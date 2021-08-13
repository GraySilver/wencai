# -*- coding:utf-8 -*-
from wencai.core.crawler import Wencai

global_cn_col = False


def set_variable(cn_col=False):
    global global_cn_col
    global_cn_col = cn_col

def get_scrape_report(query, start_date, end_date, period, benchmark):
    return Wencai(cn_col=globals()['global_cn_col']).backtest(
        query=query, start_date=start_date, end_date=end_date, period=period, benchmark=benchmark
    )


def get_strategy(query, start_date, end_date, stock_hold, upper_income, lower_income, period, fall_income,
                 day_buy_stock_num):
    return Wencai(cn_col=globals()['global_cn_col']).yieldbacktest(
        query=query, start_date=start_date, end_date=end_date, period=period, fall_income=fall_income,
        day_buy_stock_num=day_buy_stock_num, upper_income=upper_income, lower_income=lower_income, stock_hold=stock_hold
    )


def get_event_evaluate(query, start_date, end_date, period, index_code):
    return Wencai(cn_col=globals()['global_cn_col']).eventbacktest(
        query=query, start_date=start_date, end_date=end_date, period=period, index_code=index_code)

def get_lastjs(code):
    return Wencai(cn_col=globals()['global_cn_col']).lastjs(code)

def search(query):
    return Wencai().search(query_string=query)