import re
import json
import pandas as pd
from wencai.core.session import Session
from wencai.core.cons import WENCAI_CRAWLER_URL


class BackTest:

    def __init__(self, content, cn_col, execute_path, start_date, end_date):
        self.content = content['result']
        self.cn_col = cn_col
        self.execute_path = execute_path
        self.start_date = start_date
        self.end_date = end_date

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

        url = WENCAI_CRAWLER_URL['history_detail'].format(backtest_id=self.content['id'], start_date=start_date,
                                                          end_date=end_date, period=period)
        context = Session().get_driver(url, execute_path=self.execute_path)
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
