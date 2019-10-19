# -*- coding:utf-8 -*-
import logging
import datetime as dt
from time import sleep
import pandas as pd
from wencai.core.cons import WENCAI_CRAWLER_URL, WENCAI_HEADERS
from wencai.core.content import BackTest, YieldBackTest, EventBackTest
from wencai.core.cookies import WencaiCookie
from wencai.core.session import Session

pd.set_option('display.width', 2000)


class Wencai(object):
    logging.basicConfig(
        level=logging.WARNING,
        format='%(asctime)s [%(levelname)s] %(message)s',
    )

    def __init__(self, execute_path=None, cn_col=False):
        self.execute_path = execute_path
        self.obj_cookie = WencaiCookie(execute_path=execute_path)
        self.cn_col = cn_col

    def backtest(self, query, start_date, end_date, period, benchmark):
        payload = {
            "query": query,
            "start_date": start_date,
            "end_date": end_date,
            "period": period,
            "benchmark": benchmark
        }
        henxin_v = self.obj_cookie.getHexinVByJson(source='backtest')
        session = Session(update_headers=WENCAI_HEADERS['backtest'], hexin_v=henxin_v)
        r = session.post(WENCAI_CRAWLER_URL['backtest'], data=payload)
        if r.status_code == 200:
            return BackTest(content=r.json(), cn_col=self.cn_col, execute_path=self.execute_path,
                            start_date=start_date, end_date=end_date)

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
        henxin_v = self.obj_cookie.getHexinVByJson(source='backtest')
        session = Session(update_headers=WENCAI_HEADERS['backtest'], hexin_v=henxin_v)
        r = session.post(WENCAI_CRAWLER_URL['yieldbacktest'], data=payload)
        if r.status_code == 200:
            return YieldBackTest(content=r.json(), cn_col=self.cn_col, query=query, hexin_v=henxin_v,
                                 execute_path=self.execute_path,start_date=start_date,end_date=end_date)
        else:
            raise Exception(r.content.decode('utf-8'))

    def eventbacktest(self,query,index_code,period,start_date,end_date):
        payload = {
            "query": query,
            "start_date": start_date,
            "end_date": end_date,
            "period": period,
            "index_code":index_code
        }
        henxin_v = self.obj_cookie.getHexinVByJson(source='backtest')
        session = Session(update_headers=WENCAI_HEADERS['backtest'], hexin_v=henxin_v)
        r = session.post(WENCAI_CRAWLER_URL['eventbacktest'], data=payload)
        if r.status_code == 200:
            return EventBackTest(content=r.json(),cn_col=self.cn_col)
        else:
            raise Exception(r.content.decode('utf-8'))