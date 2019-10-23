## Wencai-API

#### 问财API目前需要接入chrome和chromedriver配合使用，请下载[chrome](https://www.google.cn/intl/zh-CN/chrome/)和对应的[chromedriver](https://npm.taobao.org/mirrors/chromedriver/)版本。

#### Start

```python
import wencai as wc
```

#### 初始化

```python
wc.set_variable(cn_col=True, execute_path='/Users/allen/Downloads/chromedriver')
```

**参数说明：**

- cn_col：True返回中文字段，False返回英文字段，默认false
- execute_path：chrome_driver路径，None表示chrome_driver在根路径，默认None

#### wc.get_scrape_report(回测一下)

```python
r = wc.get_scrape_report(query='上证指数上穿10日均线',
                         start_date='2019-10-01',
                         end_date='2019-10-19',
                         period='1,2,3,4',
                         benchmark='hs000300')
print(r.report_data) # 报告评级
print(r.backtest_data)	# 回测分析
print(r.condition_data)  # 准确回测参数
print(r.history_detail(period='1')) # 历史明细查询
```

**参数说明：**

- query：输入回测参数
- stime：开始日期
- etime：结束日期
- period：持股周期
- benchmark：基准指数

**Example:**

> 平均区间涨跌幅       盈亏比  次日开盘平均涨跌幅  持有期    次日高开概率  同期基准  基准上涨概率     最大涨跌幅     最小涨跌幅      上涨概率
>
> 0  0.000452  1.049851   0.000191    1  0.389201     0       0  0.101504 -0.100000  0.467942
>
> 1  0.002819  1.248264   0.000552    2  0.396705     0       0  0.210123 -0.108460  0.494297
>
> 2  0.005292  1.425027   0.001694    3  0.425254     0       0  0.330961 -0.117544  0.526851
>
> 3  0.005753  1.406133   0.002266    4  0.435000     0       0  0.377018 -0.124862  0.508333

#### wc.get_strategy(策略回测)

```python
r = wc.get_strategy(query='非停牌；非st；今日振幅小于5%；量比小于1；涨跌幅大于-5%小于1%；流通市值小于20亿；市盈率大于25小于80；主力控盘比例从大到小',
                    start_date='2018-10-09',
                    end_date='2019-07-16',
                    period='1',
                    fall_income=1,
                    lower_income=5,
                    upper_income=9,
                    day_buy_stock_num=1,
                    stock_hold=2)
print(r.profit_data) # 累计收益数据
print(r.backtest_data) # 报告评级
print(r.condition_data) # 准确回测语句
print(r.history_detail(period='1')) # 历史明细查询
print(r.history_pick(trade_date='2019-07-16', hold_num=1)) # 策略选股
```

**参数说明：**

- query：输入回测参数
- stime：开始日期
- etime：结束日期
- period：持有期
- upper_income：止盈收益持有率
- fall_income：止盈收益回落率
- lower_income：止损收益率
- day_buy_stock_num：单日买入只
- stock_hold：持股上限

**Example：**

> 涨跌幅  当日收盘价（元)   dde大单净量（%） 股本规模    股票代码 股票市场  股票名称         换手率
>
> 0  -0.10152284      9.84  -0.11978362  小盘股  002599   SZ  盛通股份  0.63294771

#### wc.get_event_evaluate(事件评级)

```python
r = wc.get_event_evaluate(end_date='2019-07-16',
                          index_code="1a0001",
                          period='1',
                          query="上证指数上穿10日均线",
                          start_date="2016-05-16")
print(r.report_data)
print(r.event_list)
```

**参数说明：**

- query：输入回测参数
- start_date：开始日期
- end_date：结束日期
- period：持有期
- index_code：对应标的

**Example：**

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