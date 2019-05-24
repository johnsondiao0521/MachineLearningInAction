#-*-coding:utf-8-*-

# 量化交易的本质
# 量化交易属于人工智能的一个应用分支，它综合了多个学科的知识和方法，用先进的数学模型代替人的主观思维制定交易策略，
# 利用计算机强大运算力从庞大的股票、债券、期货等历史数据中回测获取交易策略的盈亏“概率”，通过管理盈亏的“概率”帮助投资者做出准确的决策。
# 所谓的量化，表面上是管理盈亏的“概率”，本质上是“随时调整，合理应变”的策略。

import random
import matplotlib.pyplot as plt
import numpy as np
from timeit import timeit
import pandas as pd

def list_test():
    walk = []
    for i in range(1000000):
        walk.append(random.normalvariate(0,1))
    # plt.hist(walk,bins=30) # bins直方图的柱数
    # plt.show()
    # return None

def ndarray_test():
    # ndarray作为Numpy的核心，不仅具有矢量算术运算的能力，并且在处理多维的大规模数组时快速且节省空间。
    x = np.random.normal(loc=0.0,scale=1.0,size=1000000)
    # plt.hist(x,bins=30)
    # plt.show()

def dataframe_test():
    dd = pd.date_range('2016-01-01',freq='D',periods=1000)
    print('生成日时间序列：{}'.format(dd))


if __name__ == '__main__':
    # t1 = timeit("list_test()","from __main__ import list_test",number=1)
    # t2 = timeit("ndarray_test()","from __main__ import ndarray_test",number=1)
    # print("list:{}".format(t1))
    # print("ndarray:{}".format(t2))

    stock_data = np.random.normal(loc=0.0,scale=1.0,size=1000)
    # stock_data = np.around(stock_data,2)
    # print("stock_data:{}".format(stock_data))
    # 涨跌幅的计算公式为：(今日收盘价-昨日收盘价)/昨日收盘价*100%。
    # print("*"*100)
    # np.roll()为循环右移
    # stock_data_last = np.around(np.roll(stock_data,1),2)
    # print("stock_data_arount:{}".format(stock_data_last))

    # pct_change = np.around(((stock_data_last-stock_data)/stock_data_last),2)

    pct_change = np.around((stock_data - np.roll(stock_data, 1)) / np.roll(stock_data, 1), 2)
    pct_change[0] = np.nan
    # print("pct_change:{}".format(pct_change))
    dd = pd.date_range('2016-01-01', freq='D', periods=1000)
    stock_data = np.around(stock_data, 2)
    df_stock = pd.DataFrame({'close': stock_data, 'price range': pct_change}, index=dd)
    print(f'股价交易数据：\n {df_stock.head()}')  # 打印前5行数据

    # 绘制收盘价
    df_stock.close[100:150].plot(c='b')
    plt.legend(['Close'], loc='best')
    plt.show()


