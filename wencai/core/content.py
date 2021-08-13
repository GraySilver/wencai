import re
import json
import pandas as pd
from wencai.core.cons import WENCAI_CRAWLER_URL

pd.set_option('display.max_rows', 2000)


class BackTest:

    def __init__(self, content, cn_col, start_date, end_date, session):
        if content['errorcode'] == 1:
            raise ValueError(content['errormsg'])
        self.content = content['result']
        self.cn_col = cn_col
        self.start_date = start_date
        self.end_date = end_date
        self.session = session

    @property
    def backtest_data(self):
        _ = {'daySaleStrategy': '持有期',
             'averageChangeRate': '平均区间涨跌幅',
             'hs300AverageIncome': '同期基准',
             'highProbability': '次日高开概率',
             'averageOpenIncome': '次日开盘平均涨跌幅',
             'maxChangeRate': '最大涨跌幅',
             'minChangeRate': '最小涨跌幅',
             'averageLossRatio': '盈亏比',
             "winRate": '上涨概率',
             "hs300WinRate": '基准上涨概率',
             'changeRateGroup': '涨跌分布图'}
        data = self.content['backtestData']
        data = pd.DataFrame().from_dict(data)
        if 'changeRateGroup' in data.columns:
            del data['changeRateGroup']
        if self.cn_col:
            data = data.rename(columns=_)
        return data

    @property
    def condition_data(self):
        return self.content['conditionData']

    @property
    def report_data(self):
        data = self.content['reportData']
        _ = {
            'historyHappenCount': '历史发生次数',
            'maxAverageChangeRate': '最优平均涨跌幅',
            'maxWinRate': '最大上涨概率'
        }
        response = {'maxAverageChangeRate': data['maxAverageChangeRate'][0],
                    'maxWinRate': data['maxWinRate'][0],
                    'historyHappenCount': data['historyHappenCount']}
        if self.cn_col:
            response = {_[k]: v for k, v in response.items()}

        return response

    def history_detail(self, period, start_date=None, end_date=None):
        if start_date is None:
            start_date = self.start_date

        if end_date is None:
            end_date = self.end_date

        url = WENCAI_CRAWLER_URL['history_detail'].format(backtest_id=self.content['id'],
                                                          start_date=start_date,
                                                          end_date=str(end_date),
                                                          period=str(period))
        context = self.session.get_result(url=url, source='history_detail').text
        context = re.findall('{"result":(.*?),"errorcode":0,"errormsg":""}', context)[0]
        data = json.loads(context)
        data = pd.DataFrame().from_dict(data)
        _ = {
            'stock_code': '股票代码',
            'stock_name': '股票简称',
            "start_date": "起始时间",
            "end_date": "终止时间",
            "start_price": "起始价",
            "end_price": "终止价",
            "change_rate": "区间涨跌幅",
            "stock_market": "股票市场"
        }
        if self.cn_col:
            data = data.rename(columns=_)
        return data


class YieldBackTest:
    def __init__(self, content, cn_col, query, start_date, end_date, session):
        self.content = content['result']
        self.cn_col = cn_col
        self.query = query
        self.start_date = start_date
        self.end_date = end_date
        self.session =session

    @property
    def profit_data(self):
        hq300_data = self.content['Hq300Data']
        profit_data = self.content['profitData'][0]
        hq300_data = [{'date': i['timestamp'], 'benchmark_value': i['value']} for i in hq300_data]
        profit_data = [{'date': i[0], 'profit_value': i[1]} for i in profit_data['everydayIncome']]
        hq300_data = pd.DataFrame().from_dict(hq300_data)
        profit_data = pd.DataFrame().from_dict(profit_data)
        profit_data = pd.merge(left=hq300_data, right=profit_data, how='left', on='date')
        profit_data = profit_data.loc[:, ['date', 'benchmark_value', 'profit_value']]
        return profit_data

    @property
    def condition_data(self):
        return self.content['conditionData']

    @property
    def backtest_data(self):
        data = self.content['backtestData'][0]
        if 'profitVolatility' in data:
            del data['profitVolatility']

        _ = {
            'annualYield': '预期年化收益率',
            'averageIncome': '单次收益平均值',
            'averageLossRatio': '盈亏比',
            'daySaleStrategy': '持有期',
            'maxDrawDown': '最大回撤',
            'maxIncome': '单次最大收益值',
            'minIncome': '单次收益最小值',
            'profitVolatility': '',
            'sharpeRatio': '夏普比率',
            'totalTradeTimes': '交易次数',
            'weekWinRate': '周战胜率',
            'winRate': '成功率'
        }
        if self.cn_col:
            data = {_[k]: v for k, v in data.items()}
        return data

    @property
    def score_data(self):
        data = self.content['scoreData']
        _ = {
            'annualYield': '绝对收益',
            'maxDrawDown': '抗风险能力',
            'profitVolatility': '稳定性',
            'score': '综合得分',
            'winRate': '选股能力',
            'averageLossRatio': '盈利能力',
            'rank': '排名'
        }
        for i in ['date', 'count']:
            if i in data:
                del data[i]

        if self.cn_col:
            data = {_[k]: v for k, v in data.items()}
        return data

    def history_pick(self, trade_date, hold_num=1):
        url = WENCAI_CRAWLER_URL['history_pick'].format(trade_date=trade_date, hold_num=hold_num, query=self.query)
        context = self.session.get_result(url, source='history_detail').text
        context = re.findall('{"result":(.*?),"errorcode":0,"errormsg":""}', context)[0]
        data = json.loads(context)['stocks']
        data = pd.DataFrame().from_dict(data)

        _ = {
            'change_rate': '涨跌幅',
            'close_price': '当日收盘价（元)',
            'dde': 'dde大单净量（%）',
            "equit_scale": "股本规模",
            "turnover_rate": "换手率",
            "stock_code": "股票代码",
            "stock_market": "股票市场",
            "stock_name": "股票名称",
        }
        if self.cn_col:
            data = data.rename(columns=_)
        return data

    def history_detail(self, period, start_date=None, end_date=None):

        if start_date is None:
            start_date = self.start_date

        if end_date is None:
            end_date = self.end_date

        url = WENCAI_CRAWLER_URL['history_detail'].format(backtest_id=self.content['id'], start_date=start_date,
                                                          end_date=end_date, period=period)
        context = self.session.get_result(url, source='history_detail').text
        context = re.findall('{"result":(.*?),"errorcode":0,"errormsg":""}', context)[0]
        data = json.loads(context)
        data = pd.DataFrame().from_dict(data)
        _ = {
            'stock_code': '股票代码',
            'stock_name': '股票简称',
            "start_date": "起始时间",
            "end_date": "终止时间",
            "start_price": "起始价",
            "end_price": "终止价",
            "change_rate": "区间涨跌幅",
            "stock_market": "股票市场"
        }
        if self.cn_col:
            data = data.rename(columns=_)
        return data


class EventBackTest:
    def __init__(self, content, cn_col):
        self.cn_col = cn_col
        self.content = content['result']

    @property
    def event_list(self):
        data = self.content['data']
        data = pd.DataFrame().from_dict(data)

        _ = {
            '1day': '次日涨跌幅',
            'date': '事件日期',
            'index_code': '涉及标的'
        }
        if self.cn_col:
            data = data.rename(columns=_)
        return data

    @property
    def report_data(self):
        data = self.content['reportData']
        _ = {
            'maxChangeRate': '最大上涨概率',
            'maxTotalCount': '历史发生次数',
            'maxWinRate': '最优平均涨跌幅'
        }

        if self.cn_col:
            data = {_[k]: v for k, v in data.items()}
        return data

class LastJs:
    def __init__(self, content, code):
        index_str = 'quotebridge_v2_time_{}_last'.format(code)
        content = re.findall( index_str + '(.*)', content)[0].replace('(','').replace(')','')
        self.content = json.loads(content)[code]

    @property
    def get_data(self):
        data = self.content['data']
        data = [i.split(',') for i in data.split(';')]
        data = pd.DataFrame().from_records(data)
        return data