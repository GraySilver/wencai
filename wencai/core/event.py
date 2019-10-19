# -*- coding:utf-8 -*-
import pprint
from wencai.core.crawler import Wencai

global_execute_path = None
global_cn_col = False


def set_variable(execute_path=None,cn_col=False):
    global global_execute_path
    global_execute_path = execute_path
    global global_cn_col
    global_cn_col = cn_col
    return execute_path


def get_backtest(query, start_date, end_date, period, benchmark):
    return Wencai(execute_path=globals()['global_execute_path'],cn_col=globals()['global_cn_col']).backtest(
        query=query, start_date=start_date, end_date=end_date, period=period, benchmark=benchmark
    )
