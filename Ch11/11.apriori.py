#encoding:utf-8

from  numpy import *


def loadDataSet():
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]


def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])

    C1.sort()
    return list(map(frozenset, C1))  # use frozen set so we
    # can use it as a key in a dict

def scanD(D,Ck,minSupport):
    '''
        scanD（计算候选数据集 CK 在数据集 D 中的支持度，并返回支持度大于最小支持度 minSupport 的数据）
    :param D:
    :param Ck:
    :param minSupport:
    :return:
    '''
    # ssCnt 临时存放选数据集 Ck 的频率. 例如: a->10, b->5, c->8
    ssCnt={}
    for tid in D:
        for can in Ck:
            if can.issubset(tid):
                if can not in ssCnt:
                    ssCnt[can]=1
                else:
                    ssCnt[can]+=1
    numItems = float(len(D)) # 数据集 D 的数量
    retList=[]
    supportData={}
    for key in ssCnt:
        # 支持度 = 候选项（key）出现的次数 / 所有数据集的数量
        support=ssCnt[key]/numItems
        if support>=minSupport:
            # 在 retList 的首位插入元素，只存储支持度满足频繁项集的值
            retList.insert(0,key)
        # 存储所有的候选项（key）和对应的支持度（support）
        supportData[key]=support
    return retList,supportData

def aprioriGen(Lk,k):
    '''
      （输入频繁项集列表 Lk 与返回的元素个数 k，然后输出候选项集 Ck。
       例如: 以 {0},{1},{2} 为输入且 k = 2 则输出 {0,1}, {0,2}, {1,2}. 以 {0,1},{0,2},{1,2} 为输入且 k = 3 则输出 {0,1,2}
       仅需要计算一次，不需要将所有的结果计算出来，然后进行去重操作
       这是一个更高效的算法）
    :param Lk:
    :param k:
    :return:
    '''
    retList=[]
    lenLk=len(Lk)
    for i in range(lenLk):
        for j in range(i+1,lenLk):
            L1=list(Lk[i])[:k-2]
            L2=list(Lk[j])[:k-2]
            # print ('-----i=', i, k-2, Lk, Lk[i], list(Lk[i])[: k-2])
            # print ('-----j=', j, k-2, Lk, Lk[j], list(Lk[j])[: k-2])
            L1.sort();L2.sort()
            # 第一次 L1,L2 为空，元素直接进行合并，返回元素两两合并的数据集
            # if first k-2 elements are equal
            if L1==L2:
                retList.append(Lk[i]|Lk[j])
    return retList

def apriori(dataSet,minSupport=0.5):
    C1=createC1(dataSet)
    D=list(map(set,dataSet))
    L1,supportData=scanD(D,C1,minSupport)
    L=[L1]
    k=2
    while (len(L[k-2])>0):
        Ck=aprioriGen(L[k-2],k)
        Lk,supK=scanD(D,Ck,minSupport)
        supportData.update(supK)
        L.append(Lk)
        k+=1
    return L,supportData



if __name__ == '__main__':
    dataSet=loadDataSet()
    c1=createC1(dataSet)
    D=list(map(set,dataSet))
    L1,supportData0=scanD(D,c1,0.5)

