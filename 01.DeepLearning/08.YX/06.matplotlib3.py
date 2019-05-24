#-*-coding:utf-8-*-

#绘制K线图+移动平均线+成交量
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec#分割子图
import pandas_datareader.data as web
import datetime
import mpl_finance as mpf #替换 import matplotlib.finance as mpf

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

df_stockload = web.DataReader("600797.SS", "yahoo", datetime.datetime(2018,6,1), datetime.datetime(2019,1,1))
print(df_stockload.info())

fig = plt.figure(figsize=(8,6), dpi=100,facecolor="white")#创建fig对象

gs = gridspec.GridSpec(2, 1, left=0.06, bottom=0.15, right=0.96, top=0.96, wspace=None, hspace=0, height_ratios=[3.5,1])
graph_KAV = fig.add_subplot(gs[0,:])
graph_VOL = fig.add_subplot(gs[1,:])

#绘制K线图
mpf.candlestick2_ochl(graph_KAV, df_stockload.Open, df_stockload.Close, df_stockload.High, df_stockload.Low, width=0.5,colorup='r', colordown='g')  # 绘制K线走势

#绘制移动平均线图
df_stockload['Ma20'] = df_stockload.Close.rolling(window=20).mean()#pd.rolling_mean(df_stockload.Close,window=20)
df_stockload['Ma30'] = df_stockload.Close.rolling(window=30).mean()#pd.rolling_mean(df_stockload.Close,window=30)
df_stockload['Ma60'] = df_stockload.Close.rolling(window=60).mean()#pd.rolling_mean(df_stockload.Close,window=60)

graph_KAV.plot(np.arange(0, len(df_stockload.index)), df_stockload['Ma20'],'black', label='M20',lw=1.0)
graph_KAV.plot(np.arange(0, len(df_stockload.index)), df_stockload['Ma30'],'green',label='M30', lw=1.0)
graph_KAV.plot(np.arange(0, len(df_stockload.index)), df_stockload['Ma60'],'blue',label='M60', lw=1.0)

graph_KAV.legend(loc='best')
graph_KAV.set_title(u"600797 浙大网新-日K线")
graph_KAV.set_ylabel(u"价格")
graph_KAV.set_xlim(0, len(df_stockload.index))  # 设置一下x轴的范围
graph_KAV.set_xticks(range(0, len(df_stockload.index), 15))  # X轴刻度设定 每15天标一个日期

#绘制成交量图
graph_VOL.bar(np.arange(0, len(df_stockload.index)), df_stockload.Volume,color=['g' if df_stockload.Open[x] > df_stockload.Close[x] else 'r' for x in range(0,len(df_stockload.index))])
graph_VOL.set_ylabel(u"成交量")
graph_VOL.set_xlabel("日期")
graph_VOL.set_xlim(0,len(df_stockload.index)) #设置一下x轴的范围
graph_VOL.set_xticks(range(0,len(df_stockload.index),15))#X轴刻度设定 每15天标一个日期
graph_VOL.set_xticklabels([df_stockload.index.strftime('%Y-%m-%d')[index] for index in graph_VOL.get_xticks()])#标签设置为日期

#X-轴每个ticker标签都向右倾斜45度
for label in graph_KAV.xaxis.get_ticklabels():
   label.set_visible(False)#隐藏标注 避免重叠

for label in graph_VOL.xaxis.get_ticklabels():
   label.set_rotation(45)
   label.set_fontsize(10)#设置标签字体

plt.show()