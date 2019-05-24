#encoding:utf-8

from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer

from sklearn.preprocessing import MinMaxScaler,StandardScaler,Imputer

from sklearn.feature_selection import VarianceThreshold

from sklearn.decomposition import PCA

import numpy as np
import jieba

def dictVec():
    '''
    对字典进行特征值抽取
    :return: None
    '''
    dict=DictVectorizer(sparse=False)
    data=dict.fit_transform([{'city': '北京','temperature':100},{'city': '上海','temperature':60},{'city': '深圳','temperature':30}])
    print(dict.get_feature_names())
    print(data)
    print(dict.inverse_transform(data))
    return None


def countVec():
    '''

    :return:
    '''
    cv = CountVectorizer()
    # data = cv.fit_transform(["life is short,i like python","life is too long,i dislike python"])
    data = cv.fit_transform(["生命是短暂的，我喜欢python，生命太长，我不喜欢python"])
    print(cv.get_feature_names())
    print(data.toarray())
    return None

def cutwords():
    '''
    对中文进行分词
    :return:
    '''
    con1 = jieba.cut("今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。")
    con2 = jieba.cut("我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去。")
    con3 = jieba.cut("如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。")
    con1 = list(con1)
    con2 = list(con2)
    con3 = list(con3)
    c1 = " ".join(con1)
    c2 = " ".join(con2)
    c3 = " ".join(con3)

    return c1, c2, c3

def hanziVect():
    '''
    中文特征值化
    :return:
    '''
    c1, c2, c3 = cutwords()
    cv=CountVectorizer()
    data = cv.fit_transform([c1,c2,c3])
    print(cv.get_feature_names())
    print(data.toarray())

    return None

def tfidfVect():
    '''
    中文特征值化
    :return:
    '''
    c1, c2, c3 = cutwords()
    tf = TfidfVectorizer()
    data = tf.fit_transform([c1, c2, c3])
    print(tf.get_feature_names())
    print(data.toarray())



    return None

def mm():
    '''
    归一化处理
    :return:
    '''
    mm=MinMaxScaler(feature_range=(2,3))
    data = mm.fit_transform([[90,2,10,40],[60,4,15,45],[75,3,13,46]])
    print(data)
    return None

def stand():
    '''
    标准化缩放
    :return:
    '''
    std=StandardScaler()
    data = std.fit_transform([[ 1., -1., 3.],
                      [ 2., 4., 2.],
                      [ 4., 6., -1.]])
    print(data)
    print(std.mean_)
    return None

def im():
    """
    缺失值处理
    :return:
    """
    im=Imputer(missing_values='NaN',strategy='mean',axis=0)
    data = im.fit_transform([[1, 2],[np.nan, 3],[7, 6]])
    print(data)
    return None

def var():
    """

    :return:
    """
    var=VarianceThreshold(threshold=0.0)
    data = var.fit_transform([[0, 2, 0, 3], [0, 1, 4, 3], [0, 1, 1, 3]])
    print(data)
    return None

def pca():
    """
    主成分分析
    :return:
    """
    pca=PCA(n_components=0.9)
    data = pca.fit_transform([[2,8,4,5],
                              [6,3,0,8],
                              [5,4,9,1]])
    print(data)
    return None


if __name__ == '__main__':
    pca()