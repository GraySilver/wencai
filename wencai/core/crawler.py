# -*- coding:utf-8 -*-
import logging
import re
import pandas as pd
from wencai.core.cons import WENCAI_CRAWLER_URL, WENCAI_HEADERS
from wencai.core.content import BackTest, YieldBackTest, EventBackTest, LastJs
from wencai.core.cookies import WencaiCookie
from wencai.core.session import Session


class Wencai(object):
    logging.basicConfig(
        level=logging.WARNING,
        format='%(asctime)s [%(levelname)s] %(message)s',
    )

    def __init__(self, cn_col=False, proxies=None, verify=False):
        self.cookies = WencaiCookie()
        self.cn_col = cn_col
        self.session = Session(proxies=proxies, verify=verify)

    def backtest(self, query, start_date, end_date, period, benchmark):
        payload = {
            "query": query,
            "start_date": start_date,
            "end_date": end_date,
            "period": period,
            "benchmark": benchmark
        }

        r = self.session.post_result(source='backtest', url=WENCAI_CRAWLER_URL['backtest'], data=payload)
        if r.status_code == 200:
            print(r.json())
            return BackTest(content=r.json(), cn_col=self.cn_col, start_date=start_date, end_date=end_date,
                            session=self.session)

        else:
            raise Exception(r.content.decode('utf-8'))

    def yieldbacktest(self, query, start_date, end_date, stock_hold, upper_income, lower_income, period, fall_income,
                      day_buy_stock_num):
        payload = {
            "query": query,
            "start_date": start_date,
            "end_date": end_date,
            "period": period,
            "stock_hold": stock_hold,
            "upper_income": upper_income,
            "lower_income": lower_income,
            "fall_income": fall_income,
            "day_buy_stock_num": day_buy_stock_num
        }
        r = self.session.post_result(WENCAI_CRAWLER_URL['yieldbacktest'], data=payload,
                                     add_headers=WENCAI_HEADERS['backtest'], source='backtest')
        if r.status_code == 200:
            return YieldBackTest(content=r.json(), cn_col=self.cn_col, query=query,
                                 start_date=start_date, end_date=end_date,
                                 session=self.session)
        else:
            raise Exception(r.content.decode('utf-8'))

    def eventbacktest(self, query, index_code, period, start_date, end_date):
        payload = {
            "query": query,
            "start_date": start_date,
            "end_date": end_date,
            "period": period,
            "index_code": index_code
        }

        r = self.session.post_result(WENCAI_CRAWLER_URL['eventbacktest'], data=payload, source='eventbacktest')
        if r.status_code == 200:
            return EventBackTest(content=r.json(), cn_col=self.cn_col)
        else:
            raise Exception(r.content.decode('utf-8'))

    def lastjs(self, code):
        r = self.session.get_result(WENCAI_CRAWLER_URL['lastjs'].format(code), source='lastjs',
                                    add_headers=WENCAI_HEADERS['lastjs'])
        if r.status_code == 200:
            return LastJs(content=r.text, code=code).get_data
        else:
            raise Exception(r.content.decode('utf-8'))

    def search(self, query_string):

        payload = {
            "question": query_string,
            "page": 1,
            "perpage": 50,
            "log_info": '{"input_type": "typewrite"}',
            "source": "Ths_iwencai_Xuangu",
            "version": 2.0,
            "secondary_intent": "",
            "query_area": "",
            "block_list": "",
            "add_info": '{"urp": {"scene": 1, "company": 1, "business": 1}, "contentType": "json", "searchInfo": true}'
        }

        r = self.session.post_result(url=WENCAI_CRAWLER_URL['search'],
                                     data=payload, force_cookies=True)
        result = r.json()['data']['answer'][0]['txt'][0]['content']['components'][0]['data']['datas']

        def _re_str(x: str):
            _re = re.findall('(.*):前复权', x)
            if len(_re) >= 1:
                x = _re[-1]
            check_date = re.search(r"(\d{4}\d{1,2}\d{1,2})",x)
            if check_date is not None:
                return x.replace('[{}]'.format(check_date.group()), '')
            else:
                return x

        data = pd.DataFrame().from_dict(result)
        if not data.empty:
            columns = {i: _re_str(i) for i in data.columns}
            data = data.rename(columns=columns)
            for col in ['market_code', 'code', '关键词资讯', '涨跌幅']:
                if col in data.columns:
                    del data[col]
        return data