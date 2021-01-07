# wencai

wencai是i问财的策略回测接口的Pythonic工具包，满足量化爱好者和数据分析师在量化方面的需求。

[i问财](http://www.iwencai.net/)是同花顺旗下专业的机器人智能选股问答平台,致力于为投资者提供宏观数据、新闻资讯、A股、港美股、新三板、基金等各类理财方案。

![](https://graysliver.oss-cn-shenzhen.aliyuncs.com/iwcpage.jpg)

![](https://graysliver.oss-cn-shenzhen.aliyuncs.com/iwc_strategy.JPG)

### Latest Version

```
wencai==0.2.0
```

### Dependencies

- Python 2.x/3.x（当前测试使用Python3.5.5）
- requests>=2.14.2
- beautifulsoup4>=4.5.1
- selenium==3.141

### Special
问财API目前需要接入chrome和chromedriver配合使用，请下载[chrome](https://www.google.cn/intl/zh-CN/chrome/)和对应的[chromedriver](https://npm.taobao.org/mirrors/chromedriver/)版本，尽量更新新版本确保可以使用。

*目前我测试用的chrome_driver对应的是chrome版本是87.0.4280.88，各位按自己实际情况配合chrome和chromedriver版本*

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
wc.set_variable(cn_col=True, execute_path='/Users/allen/Downloads/chromedriver')

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
wc.set_variable(cn_col=True, execute_path='/Users/allen/Downloads/chromedriver')

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
wc.set_variable(cn_col=True, execute_path='/Users/allen/Downloads/chromedriver')

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

### Change Logs

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

