# -*- coding:utf-8 -*-


WENCAI_LOGIN_URL = {
    "scrape_transaction": 'http://www.iwencai.com/traceback/strategy/transaction',
    "scrape_report": 'http://www.iwencai.com/traceback/strategy/submit',
    'strategy': 'http://www.iwencai.com/traceback/strategy/submit',
    "search": "http://www.iwencai.com/data-robot/extract-new",
    'recommend_strategy': 'http://www.iwencai.com/traceback/list/get-strategy',
    'backtest': 'http://backtest.10jqka.com.cn/backtest/app.html#/backtest'
}

WENCAI_CRAWLER_URL = {
    'history_detail': 'http://backtest.10jqka.com.cn/tradebacktest/historydetail?\
                 sort_by=desc&id={backtest_id}&start_date={start_date}&end_date={end_date}&period={period}',
    "backtest": "http://backtest.10jqka.com.cn/backtestonce/backtest",
    "yieldbacktest": "http://backtest.10jqka.com.cn/tradebacktest/yieldbacktest",
    "history_pick": 'http://backtest.10jqka.com.cn/tradebacktest/historypick?\
                    query={query}&hold_num={hold_num}&trade_date={trade_date}',
    'eventbacktest':'http://backtest.10jqka.com.cn/eventbacktest/backtest',

}

WENCAI_HEADERS = {
    'backtest': {
        'Host': "backtest.10jqka.com.cn",
        'Origin': "http://backtest.10jqka.com.cn",
        "Referer": "http://backtest.10jqka.com.cn/backtest/app.html",
    }

}
