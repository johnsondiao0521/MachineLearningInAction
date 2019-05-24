#-*-coding:utf-8-*-

import numpy as np
import random

def test1():
    # 使用numpy生成数组,得到ndarray的类型
    t1 = np.array([1, 2, 3])
    print(t1)
    print(type(t1))

def test2():
    t2 = np.arange(10)
    print(t2)
    print(type(t2))

def test3():
    t3 = np.arange(4,10,2)
    print(t3,type(t3),t3.dtype)

def test4():
    #numpy中的数据类型
    t4 = np.array(range(1, 4), dtype="i1")
    print(t4)
    print(t4.dtype)

def test5():
    ##numpy中的bool类型
    t5 = np.array([1, 1, 0, 1, 0, 0], dtype=bool)
    print(t5)
    print(t5.dtype)



def test6():
    # 调整数据类型
    t5 = np.array([1, 1, 0, 1, 0, 0], dtype=bool)
    t6 = t5.astype("int8")
    print(t6)
    print(t6.dtype)

def test7():
    # numpy中的小数
    t7 = np.array([random.random() for i in range(10)])
    print(t7)
    print(t7.dtype)

def test8():
    t7 = np.array([random.random() for i in range(10)])
    t8 = np.round(t7,2)
    print(t7)
    print(t8)

def test9():
    t9 = np.array([[2,3,4,5,6,7],[3,4,5,6,7,8]])
    print(t9.shape)
    t99 = t9.reshape((3,4))
    print(t99)
    print(t99.flatten())

def test10():
    t10 = np.array([[2, 3, 4, 5, 6, 7], [3, 4, 5, 6, 7, 8]])
    print(t10+1)
    print(t10*3)

def test11():
    t11 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
    t12 = np.array([[11,12,13,14,15],[16,17,18,19,20]])
    print(t11+t12)
    print(t11*t12)
    return None


if __name__ == '__main__':
    test11()