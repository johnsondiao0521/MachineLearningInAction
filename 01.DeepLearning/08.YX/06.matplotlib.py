#-*-coding:utf-8-*-

import matplotlib.pyplot as plt
import tushare as ts
import pandas_datareader.data as web
import datetime
import mpl_finance as mpf

import matplotlib.gridspec as gridspec

df_stockload = web.DataReader('600797.SS','yahoo',start=datetime.datetime(2017,6,1),end=datetime.datetime(2019,1,1))
print(df_stockload.info())

fig = plt.figure(figsize=(8,6),facecolor='white') # 创建fig对象
fig.subplots_adjust(left=0.09,bottom=0.20, right=0.94,top=0.90, wspace=0.2, hspace=0)
graph_KAV = fig.add_subplot(1,1,1) # 创建子图
mpf.candlestick2_ochl(graph_KAV,df_stockload.Open,df_stockload.Close,df_stockload.High,df_stockload.Low,width=0.5,colorup='r', colordown='g') # 绘制K线走势

#绘制移动平均线图
df_stockload['Ma20'] = df_stockload.Close.rolling(window=20).mean()#pd.rolling_mean(df_stockload.Close,window=20)
df_stockload['Ma30'] = df_stockload.Close.rolling(window=30).mean()#pd.rolling_mean(df_stockload.Close,window=30)
df_stockload['Ma60'] = df_stockload.Close.rolling(window=60).mean()#pd.rolling_mean(df_stockload.Close,window=60)


gs = gridspec.GridSpec(2, 1, left=0.06, bottom=0.15, right=0.96, top=0.96, wspace=None, hspace=0, height_ratios=[3.5,1])
graph_KAV = fig.add_subplot(gs[0,:])
graph_VOL = fig.add_subplot(gs[1,:])

plt.show()



















