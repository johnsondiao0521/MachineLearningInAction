#-*-coding:utf-8-*-

# 算法交易
# 优势：
# 1.历史数据评估
# 2.执行高效
# 3.无主观情绪输入
# 4.可度量评价
# 5.交易频率

# 劣势：
# 1.成本
# 2.技巧

# 算法交易流程
# 1.提出假设
# 2.建立模型
# 3.回测验证
# 4.执行交易

# 交易策略的来源
# 1.市场微观结构研究
# 2.基金结构套利
# 3.机器学习/人工智能

# 交易策略的评估
# 1.策略基本假设
# 2.Sharp Ratio
# 3.杠杆
# 4.频率
# 5.风险
# 6.W/L
# 7.模型复杂度
# 8.最大亏损
# 9.Benchmarking

# 何谓回测：将交易策略在历史数据中进行合理验证的过程。

# 回测的意义：
# 1.策略筛选
# 2.策略优化
# 3.策略验证

import pandas_datareader.data as web
import datetime

start = datetime.datetime(2017,1,1)
end = datetime.date.today()
stock = web.DataReader("600797.SS","yahoo",start,end)
# print(stock.head(10))
# print("*"*100)
# print(stock.tail(10))

# print(stock.index)
# print(stock.columns)

# print(stock.info())

# print(stock.describe())

# （1）添加一列change，存储当日股票价格与前一日收盘价格相比的涨跌数值，即当日Close价格与上一日Close的差值，1月3日这天无上一日数据，因此出现缺失
change = stock.Close.diff()
stock["Change"] = change
print(stock.head(5))

# （2）对缺失的数据用涨跌值的均值就地替代NaN。
change = stock.Close.diff()
change.fillna(change.mean(),inplace=True)
stock["Change"] = change
print(stock.head(5))











