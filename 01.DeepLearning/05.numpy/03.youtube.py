#-*-coding:utf-8-*-

import numpy as np
from matplotlib import pyplot as plt

#英国和美国各自youtube1000的数据结合之前的matplotlib绘制出各自的评论数量的直方图

us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"

t_us = np.loadtxt(us_file_path,delimiter=",",dtype="int")
t_uk = np.loadtxt(uk_file_path,delimiter=",",dtype="int")
t_us_comment = t_us[:,-1]
t_uk_comment = t_uk[:,-1]

plt.figure(figsize=(20,8),dpi=80)
t_us_comment = t_us_comment[t_us_comment<=5000]
d = 250
print(np.max(t_us_comment),np.min(t_us_comment))
num_bis = (np.max(t_us_comment)-np.min(t_us_comment))//d
print(num_bis)
plt.xticks(range(np.min(t_us_comment),np.max(t_us_comment)+d,d))
plt.hist(t_us_comment,num_bis,normed=True)
plt.grid()
plt.show()