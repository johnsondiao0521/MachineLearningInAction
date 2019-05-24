#-*-coding:utf-8-*-

import numpy as np

us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"

def loadtxt():
    t1 = np.loadtxt(us_file_path, delimiter=",", dtype="int")
    print(t1)

    t2 = np.arange(24).reshape(4, 6)
    print(t2)
    print("*" * 100)
    print(t2.transpose())
    print(t2.T)
    print(t2.swapaxes(1, 0))

    return None

def slice():
    """
    qiepian
    :return:
    """
    t = np.loadtxt(us_file_path,delimiter=",",dtype="int")
    print(t)
    print("*" * 100)
    # print("取行:",t[2])
    # print(t[2:])
    # print("取不连续的多行:",t[[2,3]])
    # print("",t[1,:])
    # print("",t[2:,:])
    # print("",t[[1,2],0])
    # print("",t[:,1])
    # print(t[1:,[1,2]])
    # print(t[[0, 2, 2], [0, 1, 3]])
    t1 = t[t<10]=3
    print(t1)
    return None

def boolIndex():
    t = np.arange(24).reshape(4,6)
    print(t)
    print("*"*100)
    t1 = np.where(t<10,3,0)
    print(t1)
    return None

def sum():
    t = np.arange(12).reshape(3,4)
    print(t)
    print("*"*100)
    print(np.sum(t,axis=1))
    return None


def statistics():
    t = np.arange(12).reshape(2,6)
    print(t)
    print("*"*100)
    # print(np.sum(t,axis=0))
    # print(np.sum(t,axis=1))
    # print(t.mean(axis=0))
    # print(np.median(t,axis=1))
    print(t.max(axis=0))
    print(t.min(axis=0))
    print(np.ptp(t,axis=0))
    print(np.std(t,axis=0))
    return None

def fill_nan_by_column_mean(t):


    for i in range(t.shape[1]):
        now_col = t[:, i]
        nan_nums = np.count_nonzero(t[:,i][t[:,i]!=t[:,i]]) # 计算非nan的个数
        if nan_nums > 0:# 存在nan值
            now_col_not_nan = now_col[np.isnan(now_col)==False] # 求和
            now_col_mean = now_col_not_nan.mean()
            now_col[np.isnan(now_col)] = now_col_mean
    return t


if __name__ == '__main__':
    t = np.array([[0., 1., 2., 3., 4., 5.],
               [6., 7., np.nan, 9., 10., 11.],
               [12., 13., 14., np.nan, 16., 17.],
               [18., 19., 20., 21., 22., 23.]])
    print(t)
    t = fill_nan_by_column_mean(t)
    print(t)