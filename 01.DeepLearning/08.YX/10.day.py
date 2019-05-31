#-*-coding:utf-8-*-

import pandas_datareader.data as web
import datetime


cash_hold = 100000 # 初始资金
posit_num = 0 #持股数目
market_total = 0 #持股市值
skip_days=0 #持股/持币状态

def GetStockDatApi(stockName=None,stockTimeS=None,stockTimeE=None, N1=15,N2=5):

    stockdata = web.DataReader(stockName, "yahoo", stockTimeS, stockTimeE)

    stockdata['N1_High'] = stockdata.High.rolling(window=N1).max()#计算最近N1个交易日最高价
    expan_max = stockdata.Close.expanding().max()
    stockdata['N1_High'].fillna(value=expan_max,inplace=True)#目前出现过的最大值填充前N1个nan

    stockdata['N2_Low'] = stockdata.Low.rolling(window=N2).min()#计算最近N2个交易日最低价
    expan_min = stockdata.Close.expanding().min()
    stockdata['N2_Low'].fillna(value=expan_min,inplace=True)#目前出现过的最小值填充前N2个nan

    #收盘价超过N1最高价 买入股票持有
    buy_index = stockdata[stockdata.Close > stockdata.N1_High.shift(1)].index
    stockdata.loc[buy_index,'signal'] = 1
    #收盘价超过N2最低价 卖出股票持有
    sell_index = stockdata[stockdata.Close < stockdata.N2_Low.shift(1)].index
    stockdata.loc[sell_index,'signal'] = 0
    stockdata['signal'].fillna(method = 'ffill',inplace = True)
    stockdata['signal'] = stockdata.signal.shift(1)
    stockdata['signal'].fillna(method = 'bfill',inplace = True)

    return stockdata

df_stockload = GetStockDatApi("600410.SS",datetime.datetime(2018, 10, 1), datetime.datetime(2019, 4, 1))
for k1_index,today in df_stockload.iterrows():
    print(k1_index,today)
    if today.signal == 1 and skip_days == 0:#买入
        start = df_stockload.index.get_loc(k1_index)
        skip_days = -1
        posit_num = int(cash_hold/today.Close) # 资金转化为股票
        cash_hold = 0

    elif today.signal == 0 and skip_days == -1:#卖出 避免未买先卖
        end = df_stockload.index.get_loc(k1_index)
        skip_days = 0
        cash_hold = int(posit_num*today.Close)#股票转化为资金
        market_total = 0






