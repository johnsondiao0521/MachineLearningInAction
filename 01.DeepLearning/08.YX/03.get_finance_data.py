#-*-coding:utf-8-*-


import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

# Panads获取股票数据

# # 获取上证指数的2017.1.1日至今的交易数据
# df_stockload = web.DataReader('000001.SS','yahoo',datetime.datetime(2017,1,1),datetime.date.today())
# # print(df_stockload.head())
# # print(df_stockload.tail())
#
# # print(df_stockload.index)
# # print(df_stockload.columns)
#
# # 绘制收盘价
# df_stockload.Close.plot(c='b')
# plt.legend(['Close','30ave','60ave'],loc='upper right')
# plt.show()

# Tushare 获取股票数据
import tushare as ts
import pandas as pd

# old 接口
# 介绍 ts.get_hist_data()、ts.get_k_data()接口的特点
df =ts.get_hist_data('600410',start='2017-01-01',end=datetime.datetime.now().strftime('%Y-%m-%d'))
# print(df.info())
df.index=pd.to_datetime(df.index)
df.sort_index(inplace=True)
print(df.head(20))

print("=="*100)

df1 = ts.get_k_data("600410",start='2017-01-01',end=datetime.datetime.now().strftime('%Y-%m-%d'))
print(df1.head())