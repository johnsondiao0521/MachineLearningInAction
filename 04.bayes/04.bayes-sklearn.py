#!/usr/bin/python
# -*- coding:utf-8 -*-

# GaussianNB_高斯朴素贝叶斯
import numpy as np
from sklearn.naive_bayes import GaussianNB,MultinomialNB,BernoulliNB
from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

def gaussian():
    """
    GaussianNB_高斯朴素贝叶斯
    :return:
    """
    X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    Y = np.array([1, 1, 1, 2, 2, 2])
    clf = GaussianNB()
    clf.fit(X, Y)
    print(clf.predict([[-0.8, -1]]))
    clf_pf = GaussianNB()
    clf_pf.partial_fit(X, Y, np.unique(Y))
    print(clf_pf.predict([[-0.8, -1]]))
    return None

def multinomial():
    """
    MultinomialNB_多项朴素贝叶斯
    :return:
    """
    X = np.random.randint(5, size=(6, 100))
    print("X:",X)
    y = np.array([1, 2, 3, 4, 5, 6])
    clf = MultinomialNB()
    clf.fit(X, y)
    print(clf.predict(X[2:3]))
    return None

def bernoulli():
    """
    BernoulliNB_伯努利朴素贝叶斯
    :return:
    """
    X = np.random.randint(2, size=(6, 100))
    Y = np.array([1, 2, 3, 4, 4, 5])
    clf = BernoulliNB()
    clf.fit(X, Y)
    print(clf.predict(X[2:3]))
    return None

def naviebayes():
    '''
        朴素贝叶斯进行文本分类
    :return:
    '''
    news=fetch_20newsgroups(subset='all')

    # 进行数据分割
    x_train,x_test,y_train,y_test=train_test_split(news.data,news.target,test_size=0.25)

    # 对数据集进行特征抽取
    tf=TfidfVectorizer()

    # 以训练集当中的词的列表进行每篇文章重要性统计
    x_train=tf.fit_transform(x_train)
    print(tf.get_feature_names)
    print(x_train.toarray())
    x_test = tf.transform(x_test)

    # 进行朴素贝叶斯算法的预测
    mlt=MultinomialNB(alpha=1.0)
    mlt.fit(x_train,y_train)
    y_predict=mlt.predict(x_test)

    print("预测的文章类别为：",y_predict)
    # 得出准确率
    print("准确率为：",mlt.score(x_test,y_test))

    return None

if __name__ == '__main__':
    naviebayes()