# -*- coding:utf-8 -*-


WENCAI_LOGIN_URL = {
    "scrape_transaction": 'http://www.iwencai.com/traceback/strategy/transaction',
    "scrape_report": 'http://www.iwencai.com/traceback/strategy/submit',
    'strategy': 'http://www.iwencai.com/traceback/strategy/submit',
    "search": "http://www.iwencai.com/data-robot/extract-new",
    'recommend_strategy': 'http://www.iwencai.com/traceback/list/get-strategy',
    'backtest': 'http://backtest.10jqka.com.cn/backtest/app.html#/backtest',
    'lastjs':'http://x.10jqka.com.cn/stockpick?tid=stockpick&ts=1&qs=pc_~soniu~stock~stock~znxg~topbar&allow_redirect=false&zhineng=opened'
}

WENCAI_CRAWLER_URL = {
    'history_detail': 'http://backtest.10jqka.com.cn/backtestonce/historydetail?sort_by=desc&id={backtest_id}&start_date={start_date}&end_date={end_date}&period={period}',
    "backtest": "http://backtest.10jqka.com.cn/backtestonce/backtest",
    "yieldbacktest": "http://backtest.10jqka.com.cn/tradebacktest/yieldbacktest",
    "history_pick": 'http://backtest.10jqka.com.cn/tradebacktest/historypick?query={query}&hold_num={hold_num}&trade_date={trade_date}',
    'eventbacktest': 'http://backtest.10jqka.com.cn/eventbacktest/backtest',
    'lastjs':'http://d.10jqka.com.cn/v2/time/{}/last.js',
    'search': 'http://x.10jqka.com.cn/unifiedwap/unified-wap/v2/result/get-robot-data'

}

WENCAI_HEADERS = {
    'backtest': {
        'Host': "backtest.10jqka.com.cn",
        'Origin': "http://backtest.10jqka.com.cn",
        "Referer": "http://backtest.10jqka.com.cn/backtest/app.html",
    },
    'lastjs':{
        'Host': "d.10jqka.com.cn",
        # 'Origin': "http://backtest.10jqka.com.cn",
        "Referer": "http://x.10jqka.com.cn/",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    }

}
