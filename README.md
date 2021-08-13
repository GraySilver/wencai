# wencai

[![PyPi Version](https://img.shields.io/pypi/v/wencai.svg)](https://pypi.org/project/wencai/)[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)[![Linux](https://travis-ci.com/GraySilver/wencai.svg?branch=master)](https://travis-ci.org/GraySilver/wencai) 

wencai是i问财的策略回测接口的Pythonic工具包，满足量化爱好者和数据分析师在量化方面的需求。

[i问财](http://www.iwencai.net/)是同花顺旗下专业的机器人智能选股问答平台,致力于为投资者提供宏观数据、新闻资讯、A股、港美股、新三板、基金等各类理财方案。

![](https://graysliver.oss-cn-shenzhen.aliyuncs.com/iwcpage.jpg)

![](https://graysliver.oss-cn-shenzhen.aliyuncs.com/iwc_strategy.JPG)

### Latest Version

```
wencai==0.2.3
```

### Dependencies

- Python 2.x/3.x（当前测试使用Python3.5.5）
- requests>=2.14.2
- beautifulsoup4>=4.5.1
- PyExecJS>=1.5.1

### Installation

- 方式1：pip install wencai
- 方式2：git clone 此github项目，然后进入根目录后进行```python setup.py install```
- 方式3：访问<https://pypi.python.org/pypi/wencai>下载安装

### Upgrade

```shell
pip install wencai --upgrade
```

### API

具体API接口请点击这里：[Wiki](https://github.com/GraySilver/wencai/blob/master/API.md)

### Quick Start

**Example 1**. 获取回测分析

```python
import wencai as wc

# 若需中文字段则cn_col=True,chromedriver路径不在根目录下需指定execute_path
wc.set_variable(cn_col=True)

strategy = wc.get_scrape_report(query='上证指数上穿10日均线',
                                 start_date='2019-10-01',
                                 end_date='2019-10-19',
                                 period='1,2,3,4',
                                 benchmark='hs000300')

print(strategy.backtest_data)
```

> 平均区间涨跌幅       盈亏比  次日开盘平均涨跌幅  持有期    次日高开概率  同期基准  基准上涨概率     最大涨跌幅     最小涨跌幅      上涨概率
>
> 0  0.000452  1.049851   0.000191    1  0.389201     0       0  0.101504 -0.100000  0.467942
>
> 1  0.002819  1.248264   0.000552    2  0.396705     0       0  0.210123 -0.108460  0.494297
>
> 2  0.005292  1.425027   0.001694    3  0.425254     0       0  0.330961 -0.117544  0.526851
>
> 3  0.005753  1.406133   0.002266    4  0.435000     0       0  0.377018 -0.124862  0.508333



**Example 2**.获取策略

```python
import wencai as wc

# 若需中文字段则cn_col=True,chromedriver路径不在根目录下需指定execute_path
wc.set_variable(cn_col=True)

transaction = wc..get_strategy(query='非停牌；非st；今日振幅小于5%；量比小于1；涨跌幅大于-5%小于1%；流通市值小于20亿；市盈率大于25小于80；主力控盘比例从大到小',
                               start_date='2018-10-09',
                               end_date='2019-07-16',
                               period='1',
                               fall_income=1,
                               lower_income=5,
                               upper_income=9,
                               day_buy_stock_num=1,
                               stock_hold=2)

print(transaction.history_pick(trade_date='2019-07-16', hold_num=1))
```

> 涨跌幅  当日收盘价（元)   dde大单净量（%） 股本规模    股票代码 股票市场  股票名称         换手率
>
> 0  -0.10152284      9.84  -0.11978362  小盘股  002599   SZ  盛通股份  0.63294771

**Example 3**.获取事件评测

```python
import wencai as wc

# 若需中文字段则cn_col=True,chromedriver路径不在根目录下需指定execute_path
wc.set_variable(cn_col=True)

report = wc.get_event_evaluate(end_date='2019-07-16', 
                               index_code="1a0001", 
                               period='1', 
                               query="上证指数上穿10日均线",
                               start_date="2016-05-16")
print(report.event_list)
print(report.report_data)
```

> {'最大上涨概率': 9.506849315068482e-05, '最优平均涨跌幅': 0.5753424657534246, '历史发生次数': 73}

>次日涨跌幅      事件日期  涉及标的
>
>0   -0.02580  20190705  上证指数
>
>1    0.00088  20190617  上证指数
>
>2   -0.00558  20190611  上证指数
>
>3    0.00165  20190528  上证指数
>
>4   -0.00491  20190521  上证指数
>
>5    0.00580  20190515  上证指数

**Example 4**.一键搜索(目前仅能获取首页内容)

```python
import wencai as wc

result = wc.search(query="当前热股")
print(result)
```

>  开盘价           成交量      振幅     收盘价     最低价     最新价     最高价       股票代码  股票简称
>
> 0     7.21   85040786.00  19.556    8.43    7.18    8.43    8.59  300320.SZ  海达股份
> 1     3.67   77019302.00  10.354    4.04    3.66    4.04    4.04  000420.SZ  吉林化纤
> 2    12.23   59261312.00  11.318   13.61   12.21   13.61   13.61  002386.SZ  天原股份
> 3    11.10   44611374.00   7.050   11.86   11.10   11.86   11.86  000848.SZ  承德露露
> 4     9.30   29671324.00  11.915   10.34    9.22   10.34   10.34  605167.SH   利柏特
> 5    24.55   12190900.00   6.571   26.11   24.55   26.11   26.11  002895.SZ  川恒股份
> 6    35.36   35961355.00  14.455   38.57   34.77   38.57   39.88  300087.SZ  荃银高科
> 7    20.15   12087816.00  11.204   22.08   20.11   22.08   22.39  603855.SH  华荣股份
> 8    21.00   13255236.00  20.170   23.02   20.70   23.02   24.98  300602.SZ   飞荣达
> 9    23.41   19325582.00  10.612   25.24   23.21   25.24   25.69  002741.SZ  光华科技
> 10   10.33   82651901.00  11.286   11.00   10.06   11.00   11.21  002297.SZ  博云新材
> 11   25.09    6203078.00  12.292   27.13   24.56   27.13   27.66  603507.SH  振江股份
> 12   16.25   43201978.00  10.831   17.48   16.12   17.48   17.88  600452.SH  涪陵电力
> 13   86.27    3288515.00  11.776   92.90   85.99   92.90   96.20  688330.SH   宏力达
> 14   37.00  130804048.00   5.561   36.42   35.50   36.42   37.39  002601.SZ  龙佰集团
> 15   19.95   29192667.00   7.721   20.38   19.21   20.38   20.68  603393.SH  新天然气
> 16    5.85   86672750.00  11.205    6.30    5.82    6.30    6.48  601777.SH  力帆科技
> 17  105.00    2516720.00  10.397  112.88  103.01  112.88  114.00  688661.SH  和林微纳
> 18   10.16   30701521.00   9.500   10.65   10.00   10.65   10.95  600203.SH  福日电子
> 19    6.55   10837756.00   9.560    6.99    6.54    6.99    7.17  600080.SH  金花股份
> 20  291.96   11381105.00   7.957  308.18  286.60  308.18  309.89  000661.SZ  长春高新
> 21   14.27   88463034.00   5.887   15.02   14.22   15.02   15.06  600580.SH  卧龙电驱
> 22    4.74   47554251.00   9.015    5.02    4.68    5.02    5.11  002141.SZ  贤丰控股
> 23    8.21   50885073.00   8.631    8.53    8.10    8.53    8.80  002114.SZ  罗平锌电

### Change Logs

### 0.2.3 2021/08/13

- 更新Cookies机制；
- 新增分时数据接口。

### 0.2.2 2021/04/08

- 正常测试接口是否可用；
- 优化报错会直接返回接口结果；
- cookies缓存带有时效性。

### 0.2.0 2021/01/07

- 正常测试接口是否可用；
- 补充说明调用逻辑。

### 0.2.0 2019/10/19

- 重构问财接口调用逻辑；
- 新增chromedriver调用接口；
- 新增【事件评测】接口；

### 0.1.5 2018/3/5

- 修正：调用问财策略接口失败问题

### 0.1.3 2017/11/27

- 创建第一个版本

### Others
此工具包不得用于任何商业目的，仅可用于爱好量化交易者分享学习和技术讨论。

Welcome to Star and Follow~

