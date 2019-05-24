#-*-coding:utf-8-*-

# 时间序列分析

# 建立数据库的意义
# 1.建模
# 1.1 模型建立
# 1.2模型评估
# 1.3模型回测
# 1.4风险控制
# 2.交易
# 3.目的：能存、能取

import tushare as ts
ts.set_token('3164a64903343a986f4519bae82be86ce05c43e49bca898359ffbc52')

 #上证指数 深圳成指 沪深300指数 上证50 中小板 创业板
data = ts.get_realtime_quotes(['sh','sz','hs300','sz50','zxb','cyb'])
# print(data)

df = ts.get_sina_dd('600848', date='2019-05-20') #默认400手
# print(df)


# data = ts.get_industry_classified()
# print(type(data))
# print(data.head(10))

pro = ts.pro_api()

df = pro.new_share(start_date='20180901', end_date='20181018')


print(ts.get_today_all())