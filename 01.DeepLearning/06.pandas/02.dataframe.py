#-*-coding:utf-8-*-

import pandas as pd
import numpy as np


# t1 = np.arange(12).reshape(3,4)
# pf = pd.DataFrame(t1)
# print(pf)

# t2 = {"name":["xiaomin"],"age":[18],"tel":["13800"]}
# pf2 = pd.DataFrame(t2)
# print(pf2)

# t3 = [{"name":"xiaomin","age":18,"tel":"10086"},{"name":"xiaogang","age":28},{"name":"xiaowang","tel":"10087"}]
# pf3 = pd.DataFrame(t3)
# print(pf3.describe())

data = pd.read_csv("./data/dogNames2.csv")
data = data.sort_values(by="Count_AnimalName")
print(data)