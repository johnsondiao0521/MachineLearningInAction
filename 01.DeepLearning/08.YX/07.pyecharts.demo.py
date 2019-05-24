#-*-coding:utf-8

from pyecharts import Kline
import pandas_datareader.data as web
import datetime
df_stockload = web.DataReader("000001.SS", "yahoo", datetime.datetime(2018, 1, 1), datetime.datetime(2019, 1, 1))
kline = Kline("行情显示图")
# 数据转换
ohlc = list(zip(df_stockload.Open,df_stockload.Close,df_stockload.Low,df_stockload.High))
dates = df_stockload.index.strftime('%Y-%m-%d')

kline.add("日K", dates, ohlc, is_datazoom_show=True,mark_line=["max"], mark_point=["max"], xaxis_rotate=30, yaxis_min=0.9*min(df_stockload["Low"]))

kline.show_config()
kline.render(r'k.html')

