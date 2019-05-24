#-*-coding:utf-8-*-

import pandas_datareader.data as web
import datetime
import statsmodels.api as sm
from statsmodels import regression
from matplotlib import pyplot as plt
import numpy as np

# df_stockload = web.DataReader("600797.SS",'yahoo',datetime.datetime(2018,10,1), datetime.datetime(2019,4,1))
# print(df_stockload.info())

# # 股票交易需要做的有三件事：选股、择时和仓位管理。
#
# # statsmodels提供的OLS()方法用于实现多项式拟合计算，OLS（ordinary least squares）
# # 即为普通最小二乘法的缩写，此处回归模型是最基本的一元模型：
#
# x = sm.add_constant(x)
# model = regression.linear_model.OLS(y_arr,x).fit()
#
# rad = model.params[1] # y=kx+b:params[1]
# intercept = model.params[0] # y=kx+b:params[0]=b

plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False # 用来正常显示负号

df_stockload = web.DataReader("600797.SS",'yahoo',datetime.datetime(2018,10,1), datetime.datetime(2019,4,1))
# print(df_stockload.info())
df_stockload.fillna(method='bfill',inplace=True) # 后一个数据填充Nan
y_arr = df_stockload.Close.values
x_arr = np.arange(0,len(y_arr))
x_b_arr = sm.add_constant(x_arr) # 添加常数列1
model = regression.linear_model.OLS(y_arr,x_b_arr).fit() # 使用OLS做拟合

rad = model.params[1] # y=kx+b:params[1]
intercept = model.params[0] # y=kx+b:params[0]=b

reg_y_fit = x_arr*rad+intercept
#matplotlib 绘制
plt.plot(x_arr,y_arr)
plt.plot(x_arr,reg_y_fit,'r')
plt.title(u'浙大网新'+'y='+str(rad)+'*x'+str(intercept))
plt.legend(['close','linear'],loc='best')

plt.show()







