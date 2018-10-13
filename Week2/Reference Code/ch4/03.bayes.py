#encoding:utf-8
from numpy import *
def loadDataSet():
    '''创建一个实验样本，'''
    postingList=[['my','dog','has','flea','problems','help','please'],
                 ['maybe','not','take','him','to','dog','park','stupid'],
                 ['my','dalmation','is','so','cute','I','love','him'],
                 ['stop','posting','stupid','worthless','garbage'],
                 ['mr','licks','ate','my','steak','how','to','stop','him'],
                 ['quit','buying','worthless','dog','food','stupid']]
    classVec=[0,1,0,1,0,1]  # 1代表侮辱性文字，0 代表正常言论
    return postingList,classVec

def createVocabList(dataSet):
    vocabSet=set([])
    for document in dataSet:
        vocabSet=vocabSet|set(document) #创建2个集合的并集
    return list(vocabSet)

def setOfWords2Vec(vocabList,inputSet):
    returnVec=[0]*len(vocabList)    #创建一个其中所含元素都为0的向量
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)]=1
        else:
            print("the word:%s is not in my Vocabulary!"%word)
    return returnVec

def bagOfWords2VecMN(vocabList,inputSet):
    '''朴素贝叶斯词袋模型'''
    returnVec=[0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)]+=1
    return returnVec

def trainNB0(trainMatrix,trainCategory):
    '''朴素贝叶斯分类器训练函数'''
    print("=========================trainNB0=========================")
    numTrainDocs=len(trainMatrix)
    numWords=len(trainMatrix[0])
    pAbusive=sum(trainCategory) / float(numTrainDocs)
    print("sum(trainCategory):",sum(trainCategory))
    p0Num=ones(numWords);p1Num=ones(numWords)
    p0Denom=2.0;p1Denom=2.0
    for i in range(numTrainDocs):
        if trainCategory[i]==1:
            p1Num+=trainMatrix[i]
            #print("p1Num:",p1Num)
            p1Denom+=sum(trainMatrix[i])
            #print("p1Denom:",p1Denom)
        else:
            p0Num+=trainMatrix[i]
            #print("p0Num:",p0Num)
            p0Denom+=sum(trainMatrix[i])
            #print("p0Denom:",p0Denom)
    p1Vect=p1Num/p1Denom
    p0Vect=p0Num/p0Denom
    return p0Vect,p1Vect,pAbusive

def classifyNB(vec2Classify,p0Vec,p1Vec,pClass1):
    '''朴素贝叶斯分类函数'''
    p1=sum(vec2Classify*p1Vec)+log(pClass1) # 元素相乘
    p0=sum(vec2Classify*p0Vec)+log(1.0-pClass1) #元素相乘
    if p1 > p0:
        return 1
    else:
        return 0

def testingNB():
    listOPosts,listClass=loadDataSet()
    myVocabList=createVocabList(listOPosts)
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList,postinDoc))
    p0V,p1V,pAb=trainNB0(array(trainMat),array(listClass))
    testEntity=['love','my','dalmation']
    thisDoc=array(setOfWords2Vec(myVocabList,testEntity))
    print("thisDoc:",thisDoc)
    print("thisDoc*p0Vec:", thisDoc*p0V)
    print("thisDoc*p1Vec:", thisDoc * p1V)
    print(testEntity,'classified as:',classifyNB(thisDoc,p0V,p1V,pAb))
    testEntity=['stupid','garbage']
    thisDoc=array(setOfWords2Vec(myVocabList,testEntity))
    print("*"*40)
    print("thisDoc:", thisDoc)
    print("thisDoc*p0Vec:", thisDoc * p0V)
    print("thisDoc*p1Vec:", thisDoc * p1V)
    print(testEntity,'classify as:',classifyNB(thisDoc,p0V,p1V,pAb))

def textParse(bigString):
    import re
    listOfTokens=re.split(r'\W*',bigString)
    return [tok.lower() for tok in listOfTokens if len(tok)>2]

def spamTest():
    docList=[];classList=[];fullText=[]
    for i in range(1,26):
        wordList=textParse(open('email/spam/%d.txt'%i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList=textParse(open('email/ham/%d.txt'%i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList=createVocabList(docList)
    trainingSet=range(50);testSet=[]
    for i in range(10):
        randIndex=int(random.uniform(0,len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del (trainingSet[randIndex])
    trainMat=[];trainClasses=[]
    for docIndex in trainingSet:
        trainMat.append(setOfWords2Vec(vocabList,docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V,p1V,pSpam=trainNB0(array(trainMat),array(trainClasses))
    errorCount=0
    for docIndex in testSet:
        wordVector=setOfWords2Vec(vocabList,docList[docIndex])
        if classifyNB(array(wordVector),p0V,p1V,pSpam)!=classList[docIndex]:
            errorCount+=1
    print('the error rate is:',float(errorCount)/len(testSet))

def calcMostFreq(vocabList,fullText):
    '''RSS源分类器及高频词去除函数'''
    import operator
    freqDict={}
    for token in vocabList:
        freqDict[token]=fullText.count(token)
    sortedFreq=sorted(freqDict.items(),key=operator.itemgetter(1),reverse=True)
    return sortedFreq[:30]

def localWords(feed1,feed0):
    import feedparser
    docList=[];classList=[];fullText=[];
    minLen=min(len(feed1['entries']),len(feed0['entries']))
    for i in range(minLen):
        wordList=textParse()


if __name__ == '__main__':
    import feedparser
    ny=feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
    print(ny)
    print(len(ny))
    #testingNB()
    # listOPosts,listClass=loadDataSet()
    # myVocabList=createVocabList(listOPosts)
    # print("listClass:",listClass)
    # print("listOPosts:",listOPosts)
    # print("myVocabList:",myVocabList)
    # # returnVec=setOfWords2Vec(myVocabList,listOPosts[0])
    # # print("returnVec:",returnVec)
    # trainMat=[]
    # i=0
    # for postinDoc in listOPosts:
    #     i+=1
    #     returnVec=setOfWords2Vec(myVocabList,postinDoc)
    #     print("returnVec:",i,returnVec)
    #     trainMat.append(returnVec)
    # print("trainMat:",trainMat)
    # p0V,p1V,pAb=trainNB0(trainMat,listClass)
    # print("p0V:",p0V)
    # print("p1V:",p1V)
    # print("pAb:",pAb)
