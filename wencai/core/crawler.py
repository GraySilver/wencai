# -*- coding:utf-8 -*-
import logging
import pandas as pd
from wencai.core.cons import WENCAI_CRAWLER_URL, WENCAI_HEADERS
from wencai.core.content import BackTest, YieldBackTest, EventBackTest, LastJs
from wencai.core.cookies import WencaiCookie
from wencai.core.session import Session

pd.set_option('display.width', 2000)


class Wencai(object):
    logging.basicConfig(
        level=logging.WARNING,
        format='%(asctime)s [%(levelname)s] %(message)s',
    )

    def __init__(self, cn_col=False):
        self.cookies = WencaiCookie()
        self.cn_col = cn_col
        self.session = Session()

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
