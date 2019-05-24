#encoding:utf-8

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

def test_iris():
    iris = load_iris()
    x_train, x_test, y_train, y_test = train_test_split(iris.data,iris.target,train_size=0.9)
    print(x_train,y_train)

def knncls():
    """
    K-近邻预测用户签到位置
    :return:None
    """
    return None

def test():
    pass

if __name__ == '__main__':
    pass
