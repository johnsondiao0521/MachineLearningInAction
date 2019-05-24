#-*-coding:utf-8-*-

import pandas as pd
import numpy as np
import string

from pymongo import MongoClient


# t1 = pd.Series(np.arange(10),index=list(string.ascii_lowercase[:10]))
# print(t1)
#
# index=list(string.ascii_lowercase)
# print(index)

# a = {string.ascii_lowercase[i]:i for i in range(10)}
# t1 = pd.Series(a)
# print(t1)
# print("*"*100)
# print(t1.index)

# #pandas读取csv中的文件
# df = pd.read_csv("./data/dogNames2.csv")
# print(df[(800<df["Count_AnimalName"])|(df["Count_AnimalName"]<1000)])

client = MongoClient()
collection = client["douban"]["tv1"]
data = collection.find()
t1 = data[0]
t1 = pd.Series(t1)
print(t1)