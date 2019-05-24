#-*-coding:utf-8-*-

import pandas_datareader.data as web
import datetime

df_stockload = web.DataReader("600410.SS", "yahoo", datetime.datetime(2018,10,1), datetime.datetime(2019,4,1))
# print(df_stockload.describe())

# 关于参数N1、N2的选取，假定我们侧重于中线周期的交易，此处选择N1参数为15天，N2参数为5天，
# 至于参数N1大于N2的原因是为了打造一个非均衡胜负收益的环境，因为我们从事量化交易的目标是要赢钱比亏钱要多。
N1 = 15
N2 = 5
df_stockload['N1_High'] = df_stockload.High.rolling(window=N1).max() # 计算最近N1个交易日最高价
print(df_stockload.info())