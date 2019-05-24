#-*-coding:utf-8-*-

import numpy as np

def test1():
    us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
    uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"

    us_data = np.loadtxt(us_file_path, delimiter=",", dtype="int")
    uk_data = np.loadtxt(uk_file_path, delimiter=",", dtype="int")

    zeros_data = np.zeros((us_data.shape[0], 1)).astype("int")
    ones_data = np.ones((uk_data.shape[0], 1)).astype("int")

    us_data = np.hstack((us_data, zeros_data))
    uk_data = np.hstack((uk_data, ones_data))

    final_data = np.vstack((us_data, uk_data))
    print(final_data)
    return None

def test2():
    t1 = np.arange(12).reshape(3,4)
    t2 = np.arange(12,24).reshape(3,4)
    t3 = np.vstack((t1,t2))
    print(t3)
    return None

def test3():
    t1 = np.random.rand(3,4)
    t2 = np.random.randn(3,3,3)
    print(t2)

if __name__ == '__main__':
    test3()