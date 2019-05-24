#-*-coding:utf-8-*-

import pandas_datareader.data as web
import datetime

df_stockload = web.DataReader('000001.SS','yahoo',start=datetime.datetime(2018,1,1),end=datetime.datetime(2018, 2, 1))
# print(df_stockload.values)

# 行/列索引
def test1():
    # 在pandas中DataFrame.index可以访问DataFrame全部的行索引，DataFrame.columns可以访问DataFrame全部的列索引，接下来我们用例程来分别展示下访问行/列索引的方法。
    print(df_stockload.index)
    print(df_stockload.columns)

    # 用DataFrame.axes查看交易数据行和列的轴标签基本信息，DataFrame.axes等价于DataFrame.index结合DataFrame.columns
    print(df_stockload.axes)

# 行/列元素访问
def test2():
    # DataFrame.values可以访问DataFrame全部元素数值，以numpy.ndarray数据类型返回
    # print(df_stockload.values)
    # print(type(df_stockload.values))

    #假如我们要访问DataFrame的某列内容，可以通过类似字典标记的方式或属性的方式，指定列索引来访问DataFrame的某列内容，
    # 比如DataFrame['Open']或是DataFrame.Open方式访问'Open'列的元素，返回得到的'Open'列元素其实是Series数据结构，
    # 所以我们也可以把 DataFrame 看成是共享同一个 index 的 Series 数据结构的集合
    # print(df_stockload['Open'])
    # print(type(df_stockload['Open']))

    print(df_stockload[0:1])

# 元素级的访问
def test3():
    # loc是通过标签方式选取数据，iloc是通过位置方式选取数据，ix则是结合loc和iloc的特点，采用混合标签和位置的方式访问元素。
    # print(df_stockload.loc['2018-01-02',['High','Low']])
    # print(df_stockload.iloc[0:2,2:5])
    # print(df_stockload.ix[[0, 2], 'High'])

    # 当使用loc前，需要将位置形式的行索引转换为标签形式的行索引后，再使用loc方法，如DataFrame.index[[0, 2]]将位置'0, 2'转换为标签'2018-01-02', '2018-01-04'，如下所示：
    print(df_stockload.loc[df_stockload.index[[0, 2]], 'High'])

    # 当使用iloc前，需要将标签形式的列索引转换为位置形式的列索引，再使用iloc方法，如下所示：
    print(df_stockload.iloc[[0,2],df_stockload.columns.get_loc('High')])

def test4():
    # 单均线突破的交易策略为：若昨日收盘价高出过去20日平均价则今天开盘即买入股票；若昨日收盘价低于过去20日平均价，那么今天开盘卖出股票。

    # 获取上证指数交易数据 pandas-datareade模块data.DataReader()方法
    df_stockload1 = web.DataReader("000001.SS", "yahoo", datetime.datetime(2018, 1, 1), datetime.datetime(2019, 1, 1))
    df_stockload1['Ma20'] = df_stockload1.Close.rolling(window=20).mean()
    df_stockload1.dropna(axis=0,how='any',inplace=True)
    # print(df_stockload1.head(21))
    print(df_stockload1.head(20))

if __name__ == '__main__':
    test4()