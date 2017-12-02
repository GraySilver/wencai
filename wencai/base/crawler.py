# -*- coding:utf-8 -*-
import logging
import datetime as dt
from time import sleep
import pandas as pd
from wencai.base.cons import WENCAI_URL,WENCAI_ENGLISH_CHINESE
from wencai.base.session import Session
pd.set_option('display.width',2000)



class Wencai(object):
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
    )

    def __init__(self,*args,**kwargs):
        self.session = Session()()
        params = kwargs.keys()
        if 'stime' in params and kwargs['stime'] !=None:

            self.stime = kwargs['stime']
        else:

            self.stime = str(dt.date.today() - dt.timedelta(30))

        if 'etime' in params and kwargs['etime'] !=None:
            self.etime = kwargs['etime']
        else:
            self.etime = str(dt.date.today())

        if 'hold_for' in params:
            if isinstance(kwargs['hold_for'],int):
                self.hold_for = kwargs['hold_for']
            else:
                raise ValueError(valueErrorString('hold_for','int'))
        else:
            self.hold_for = 3

        if 'stockHoldCount' in params:
            if isinstance(kwargs['stockHoldCount'],int):
                self.stockHoldCount = kwargs['stockHoldCount']
            else:
                raise ValueError(valueErrorString('stockHoldCount','int'))
        else:
            self.stockHoldCount = 2

        if 'lowerIncome' in params:
            if isinstance(kwargs['lowerIncome'],int):
                self.lowerIncome = kwargs['lowerIncome']
            else:
                raise ValueError(valueErrorString('lowerIncome','int'))
        else:
            self.lowerIncome = 10

        if 'upperIncome' in params:
            if isinstance(kwargs['upperIncome'], int):
                self.upperIncome = kwargs['upperIncome']
            else:
                raise ValueError(valueErrorString('upperIncome', 'int'))
        else:
            self.upperIncome = 6


        self.fell = 0.001

        if 'fallIncome' in params:
            if isinstance(kwargs['fallIncome'], int):
                self.fallIncome = kwargs['fallIncome']
            else:
                raise ValueError(valueErrorString('fallIncome', 'int'))
        else:
            self.fallIncome = 6

    # 交易记录
    def scrape_transaction(self, query):
        payload = {
            'stime': self.stime,
            'etime': self.etime,
            'hold_for': self.hold_for,
            'sort': 'desc',
            'title': 'bought_at',
            'stockHoldCount': self.stockHoldCount,
            'fallIncome': self.fallIncome,
            'lowerIncome': self.lowerIncome,
            'upperIncome': self.upperIncome,
            'fell': self.fell,
            'startDate': self.stime,
            'endDate': self.etime,
            'daysForSaleStrategy': self.hold_for,
            'query': query,
            'newType': 0
        }

        try:
            resp = self.session.post(WENCAI_URL['scrape_transaction'], data = payload)
            sleep(1)
            transaction_data = resp.json()['data']
            if resp.status_code == 200 and len(transaction_data)==0:
                return pd.DataFrame()
            else:
                df = pd.DataFrame()
                for i in transaction_data:
                    sub = pd.DataFrame().from_dict(i, orient='index').T
                    df = df.append(sub, ignore_index=True)
                columns = ['stock_code',
                           'bought_at',
                            'buying_price',
                           'sold_at',
                           'selling_price',
                           'hold_for',
                           'signal_return_rate']
                df = df.sort_values(by='bought_at').astype('str').reset_index(drop=True)
                df['signal_return_rate'] = df['signal_return_rate'].apply(lambda x:'{}%'.format(x))
                columnsCn = {u:WENCAI_ENGLISH_CHINESE[u] for u in columns}
                return df.ix[:, columns].rename(columns=columnsCn).reset_index(drop=True)

        except Exception as e:
            logging.exception(e)
            return

    def strategy(self, query):
        payload = {
            'query': query,
            'daysForSaleStrategy': str(self.hold_for),
            'startDate': self.stime,
            'endDate': self.etime,
            'fell': self.fell,
            'upperIncome': self.upperIncome,
            'lowerIncome': self.lowerIncome,
            'fallIncome': self.fallIncome,
            'stockHoldCount': self.stockHoldCount
        }
        # try:
        response = self.session.post(WENCAI_URL['strategy'], data=payload)
        sleep(1)
        json_data = response.json()
        # print(json_data)
        if json_data['success'] == True:
            data = json_data['data']['stockData']['list']
            if response.status_code != 200 or 'data' not in data.keys():
                return pd.DataFrame()
            else:
                data = data['data']
                df = pd.DataFrame().from_dict(data)
                del df['__code']
                df['date'] = str(dt.date.today())
                columns = ['date', 'code', 'codeName', 'zdf', 'spj', 'dde', 'gbgm', 'hsl']
                columnsCn = {u:WENCAI_ENGLISH_CHINESE[u] for u in columns}
                return df.ix[:, columns].rename(columns=columnsCn).reset_index(drop=True)
        else:
            print('Response is false,Please try again')

        # except Exception as e:
        #     logging.exception(e)
        #     print(e)
        #     return

    # 报告评级
    def scrape_report(self, query):

        payload = {
            'query': query,
            'daysForSaleStrategy': str(self.hold_for),
            'startDate': self.stime,
            'endDate': self.etime,
            'fell': self.fell,
            'upperIncome': self.upperIncome,
            'lowerIncome': self.lowerIncome,
            'fallIncome': self.fallIncome,
            'stockHoldCount': self.stockHoldCount
        }

        try:
            response = self.session.post(WENCAI_URL['scrape_report'], data=payload)
            sleep(1)
            json_data = response.json()
            # 最大预期年化收益率: annual_yield, 最大成功率: win_rate
            df =  pd.DataFrame().from_dict(json_data['data']['result']['data']['none']['summary']).T
            df['stime'] = [self.stime]
            df['etime'] = [self.etime]
            df['annualYield'] = df['annualYield'].apply(lambda x:'{}%'.format(round(float(x) * 100, 2)))
            df['winRate'] = df['winRate'].apply(lambda x:'{}%'.format(round(float(x) * 100, 2)))
            df['sharpeRatio'] = df['sharpeRatio'].apply(lambda x:round(float(x), 2))
            df['totalTradeTimes'] = df['totalTradeTimes'].astype('str')
            df['daySaleStrategy'] = df['daySaleStrategy'].astype('str')
            df['maxDrawDown'] = df['maxDrawDown'].apply(lambda x:'{}%'.format(round(float(x) * 100, 2)))
            columns = ['stime','etime','annualYield','maxDrawDown','winRate'
                ,'weekWinRate','averageIncome','averageLossRatio','daySaleStrategy','maxIncome','minIncome',
                       'sharpeRatio','totalTradeTimes']
            columnsCn = {u: WENCAI_ENGLISH_CHINESE[u] for u in columns}
            return df.ix[:, columns].rename(columns=columnsCn).reset_index(drop=True)
        except Exception as e:
            logging.exception(e)
            return

def valueErrorString(x,ktype):
    return '{} format is {}'.format(x,ktype)



if __name__ == '__main__':
    event = Wencai()
    data = event.scrape_report('跳空高开,平台突破,非涨停,股价大于ma120,ma30ma120ma250上移,股价大于前30日最高价,非银行版块')
    print(data)



