# -*- coding:utf-8 -*-
import pprint
from wencai.core.crawler import Wencai

global_execute_path = None
global_cn_col = False


def set_execute_path(execute_path=None):
    global global_execute_path
    global_execute_path = execute_path
    return execute_path


def set_cn(cn_col=False):
    global global_cn_col
    global_cn_col = cn_col
    return cn_col


def get_backtest(query, start_date, end_date, period, benchmark):
    return Wencai(execute_path=globals()['global_execute_path'],cn_col=globals()['global_cn_col']).backtest(
        query=query, start_date=start_date, end_date=end_date, period=period, benchmark=benchmark
    )
