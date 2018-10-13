#encoding:utf-8

from math import log
import operator

def calcShannonEnt(dataSet):
    '''计算给定数据集的香农熵'''
    numEntries=len(dataSet)
    labelCounts={}
    for featVec in dataSet:
        currentLabel=featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel]=0
        labelCounts[currentLabel]+=1
    shannonEnt=0.0
    for key in labelCounts:
        prob=float(labelCounts[key])/numEntries
        shannonEnt-=prob*log(prob,2)#以2为底求对数
    return shannonEnt

def createDataSet():
    '''创建数据集'''
    dataSet=[[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
    labels=['no surfacing','flippers']
    return dataSet,labels

def splitDataSet(dataSet,axis,value):
    '''按照给定特征划分数据集'''
    retDataSet=[]
    for featVec in dataSet:
        if featVec[axis]==value:
            reducedFeatVec=featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

def chooseBestFeatureToSplit(dataSet):
    numFeatures=len(dataSet[0])-1
    baseEntropy=calcShannonEnt(dataSet)
    bestInfoGain=0.0;bestFeature=-1
    for i in range(numFeatures):
        featList=[example[i] for example in dataSet]
        print("featList=",featList)
        uniqueVals=set(featList)
        newEntropy=0.0
        for value in uniqueVals:
            subDataSet=splitDataSet(dataSet,i,value)
            prob=len(subDataSet)/float(len(dataSet))
            newEntropy+=prob*calcShannonEnt(subDataSet)
        infoGain=baseEntropy-newEntropy
        if (infoGain>bestInfoGain):
            bestInfoGain=infoGain
            bestFeature=i
    return bestFeature

def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote]=0
        classCount[vote]+=1
    sortedClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def createTree(dataSet,labels):
    '''创建树的函数代码'''
    classList=[example[-1] for example in dataSet]
    if classList.count(classList[0])==len(classList):#类别完全相同则停止继续划分
        return classList[0]
    if len(dataSet[0])==1:# 遍历完所有特征时返回出现次数最多的类别
        return majorityCnt(classList)
    bestFeat=chooseBestFeatureToSplit(dataSet)
    bestFeatLabel=labels[bestFeat]
    myTree={bestFeatLabel:{}}
    del (labels[bestFeat])
    featValues=[example[bestFeat] for example in dataSet]
    uniqueVals=set(featValues)
    for value in uniqueVals:
        subLabels=labels[:]
        myTree[bestFeatLabel][value]=createTree(splitDataSet(dataSet,bestFeat,value),subLabels)
    return myTree

def classify(inputTree,featLabels,testVec):
    '''使用决策树的分类函数'''
    firstStr=inputTree.keys()[0]
    secondDict=inputTree[firstStr]
    featIndex=featLabels.index(firstStr)
    for key in secondDict.keys():
        if testVec[featIndex]==key:
            if type(secondDict[key]).__name__=="dict":
                classLabel=classify(secondDict[key],featLabels,testVec)
            else:
                classLabel=secondDict[key]
    return classLabel

def retrieveTree(i):
    listOfTrees=[{'no surfacing':{0:'no',1:{'flippers':{0:'no',1:'yes'}}}},{'no surfacing':{0:'no',1:{'flippers':{0:{'head':{0:'no',1:'yes'}},1:'no'}}}}]
    return listOfTrees[i]

def storeTree(inputTree,filename):
    import pickle
    fw=open(filename,"wb")
    pickle.dump(inputTree,fw)
    fw.close()

def grabTree(filename):
    import pickle
    fr=open(filename,"rb")
    return pickle.load(fr)



if __name__ == '__main__':
    myTree=retrieveTree(0)
    storeTree(myTree,"classifierStorage.txt")
    tree=grabTree("classifierStorage.txt")
    print(tree)
    print("#"*30)

    myDat,labels=createDataSet()
    myDat[0][-1]='maybe'
    result=calcShannonEnt(myDat)
    print(result)
    print("#"*30)
    myDat, labels = createDataSet()
    print(myDat)
    result=splitDataSet(myDat,1,0)
    print(result)
    print("#" * 30)
    myDat, labels = createDataSet()
    result=chooseBestFeatureToSplit(myDat)
    print("result=",result)
    print("#"*30)
    result=createTree(myDat,labels)
    print("result=",result)
    print("#"*30)
    #result=classify()
