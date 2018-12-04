#encoding:utf-8

import numpy as np

"""
贝叶斯公式
p(xy)=p(x|y)p(y)=p(y|x)p(x)
p(x|y)=p(y|x)p(x)/p(y)
"""

# ------项目案例1: 屏蔽社区留言板的侮辱性言论------

def loadDataSet():
    '''
    创建数据集,都是假的 fake data set
    :return: 单词列表postinglist, 所属类别classvec
    '''
    postingList=[['my','dog','has','flea','problems','help','please'],
                 ['maybe','not','take','him','to','dog','park','stupid'],
                 ['my','dalmation','is','so','cute','I','love','him'],
                 ['stop','posting','stupid','worthless','garbage'],
                 ['mr','licks','ate','my','steak','how','to','stop','him'],
                 ['quit','buying','worthless','dog','food','stupid']]
    classVec=[0,1,0,1,0,1]  # 1代表侮辱性文字，0 代表正常言论
    return postingList,classVec

def createVocabList(dataSet):
    """
    获取所有单词的集合
    :param dataSet:数据集
    :return:所有单词的集合(即不含重复元素的单词列表)
    """
    vocabSet=set([])
    for document in dataSet:
        # | 求两个集合的并集
        vocabSet=vocabSet|set(document)
    return list(vocabSet)

def setOfWords2Vec(vocabList,inputSet):
    """
    遍历查看该单词是否出现，出现该单词则将该单词置1
    :param vocabList:所有单词集合列表
    :param inputSet:输入数据集
    :return:匹配列表[0,1,0,1...]，其中 1与0 表示词汇表中的单词是否出现在输入的数据集中
    """
    # 创建一个和词汇表等长的向量，并将其元素都设置为0
    returnVec=[0]*len(vocabList)
    # 遍历文档中的所有单词，如果出现了词汇表中的单词，则将输出的文档向量中的对应值设为1
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)]=1
        else:
            print("the word:%s is not in my Vocabulary!"%word)
    return returnVec

def _trainNaiveBayes(trainMatrix,trainCategory):
    """
    朴素贝叶斯分类器训练函数(朴素贝叶斯分类原版)
    :param trainMatrix:type is ndarray,总的输入文本，大致是 [[0,1,0,1], [], []]
    :param trainCategory:文件对应的类别分类， [0, 1, 0],列表的长度应该等于上面那个输入文本的长度
    :return:
    """
    # 文档的样本数
    numTrainDocs=len(trainMatrix)
    numWords=len(trainMatrix[0])

    # 因为侮辱性的被标记为了1， 所以只要把他们相加就可以得到侮辱性的有多少
    # 侮辱性文件的出现概率，即trainCategory中所有的1的个数
    # 代表的就是多少个侮辱性文件，与文件的总数相除就得到了侮辱性文件的出现概率

    pAbusive=np.sum(trainCategory) / float(numTrainDocs)
    # print("sum(trainCategory):",sum(trainCategory))
    # 单词出现的次数
    # 原版
    p0Num=np.zeros(numWords)
    p1Num=np.zeros(numWords)
    # 整个数据集单词出现的次数（原来是0，后面改成2了）
    p0Denom=0.0;p1Denom=0.0
    for i in range(numTrainDocs):
        # 遍历所有的文件，如果是侮辱性文件，就计算此侮辱性文件中出现的侮辱性单词的个数
        if trainCategory[i]==1:
            p1Num+=trainMatrix[i]
            p1Denom+=sum(trainMatrix[i])
            # print("p1Denom:",p1Denom)
        else:
            p0Num+=trainMatrix[i]
            #print("p0Num:",p0Num)
            p0Denom+=sum(trainMatrix[i])
            #print("p0Denom:",p0Denom)
    # 后面需要改成改成取 log 函数
    p1Vect=p1Num/p1Denom
    p0Vect=p0Num/p0Denom
    return p0Vect,p1Vect,pAbusive

def trainNaiveBayes(trainMatrix,trainCategory):
    """
    朴素贝叶斯分类修正版，　注意和原来的对比，为什么这么做可以查看书
    :param trainMatrix:type is ndarray,总的输入文本，大致是 [[0,1,0,1], [], []]
    :param trainCategory:文件对应的类别分类， [0, 1, 0],列表的长度应该等于上面那个输入文本的长度
    :return:
    """
    # 文档的样本数
    numTrainDocs=len(trainMatrix)
    numWords=len(trainMatrix[0])

    # 因为侮辱性的被标记为了1， 所以只要把他们相加就可以得到侮辱性的有多少
    # 侮辱性文件的出现概率，即trainCategory中所有的1的个数
    # 代表的就是多少个侮辱性文件，与文件的总数相除就得到了侮辱性文件的出现概率

    pAbusive=np.sum(trainCategory) / float(numTrainDocs)
    # print("sum(trainCategory):",sum(trainCategory))
    # 单词出现的次数
    # 变成ones是修改版，这是为了防止数字过小溢出
    p0Num=np.ones(numWords)
    p1Num=np.ones(numWords)
    # 整个数据集单词出现的次数（原来是0，后面改成2了）
    p0Denom=2.0;p1Denom=2.0
    for i in range(numTrainDocs):
        # 遍历所有的文件，如果是侮辱性文件，就计算此侮辱性文件中出现的侮辱性单词的个数
        if trainCategory[i]==1:
            p1Num+=trainMatrix[i]
            p1Denom+=sum(trainMatrix[i])
            # print("p1Denom:",p1Denom)
        else:
            p0Num+=trainMatrix[i]
            #print("p0Num:",p0Num)
            p0Denom+=sum(trainMatrix[i])
            #print("p0Denom:",p0Denom)
    # 后面需要改成改成取 log 函数
    p1Vect=p1Num/p1Denom
    p0Vect=p0Num/p0Denom
    return p0Vect,p1Vect,pAbusive

def classifyNaiveBayes(vec2Classify,p0Vec,p1Vec,pClass1):
    '''
    使用算法：
        # 将乘法转换为加法
        乘法：P(C|F1F2...Fn) = P(F1F2...Fn|C)P(C)/P(F1F2...Fn)
        加法：P(F1|C)*P(F2|C)....P(Fn|C)P(C) -> log(P(F1|C))+log(P(F2|C))+....+log(P(Fn|C))+log(P(C))
    :param vec2Classify:待测数据[0,1,1,1,1...]，即要分类的向量
    :param p0Vec: 类别0，即正常文档的[log(P(F1|C0)),log(P(F2|C0)),log(P(F3|C0)),log(P(F4|C0)),log(P(F5|C0))....]列表
    :param p1Vec: 类别1，即侮辱性文档的[log(P(F1|C1)),log(P(F2|C1)),log(P(F3|C1)),log(P(F4|C1)),log(P(F5|C1))....]列表
    :param pClass1:类别1，侮辱性文件的出现概率
    :return: 类别1 or 0
    '''
    # 计算公式  log(P(F1|C))+log(P(F2|C))+....+log(P(Fn|C))+log(P(C))
    # 使用 NumPy 数组来计算两个向量相乘的结果，这里的相乘是指对应元素相乘，即先将两个向量中的第一个元素相乘，然后将第2个元素相乘，以此类推。
    # 我的理解是：这里的 vec2Classify * p1Vec 的意思就是将每个词与其对应的概率相关联起来
    # 可以理解为 1.单词在词汇表中的条件下，文件是good 类别的概率 也可以理解为 2.在整个空间下，文件既在词汇表中又是good类别的概率
    p1=sum(vec2Classify*p1Vec)+np.log(pClass1) # 元素相乘
    p0=sum(vec2Classify*p0Vec)+np.log(1.0-pClass1) #元素相乘
    if p1 > p0:
        return 1
    else:
        return 0

def bagOfWords2VecMN(vocabList,inputSet):
    '''朴素贝叶斯词袋模型'''
    # 注意和原来的做对比
    returnVec=[0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)]+=1
        else:
            print('the word: {} is not in my vocabulary'.format(word))
    return returnVec

def testingNaiveBayes():
    """
    测试朴素贝叶斯算法
    :return:
    """
    # 1. 加载数据集
    listOPosts,listClass=loadDataSet()

    # 2. 创建单词集合
    vocab_list=createVocabList(listOPosts)

    # 3. 计算单词是否出现并创建数据矩阵
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(vocab_list,postinDoc))

    # 4. 训练数据
    p0V,p1V,p_abusive=trainNaiveBayes(np.array(trainMat),np.array(listClass))

    test_one = ['love', 'my', 'dalmation']
    test_one_doc = np.array(setOfWords2Vec(vocab_list, test_one))
    print('the result is: {}'.format(classifyNaiveBayes(test_one_doc, p0V, p1V, p_abusive)))
    test_two = ['stupid', 'garbage']
    test_two_doc = np.array(setOfWords2Vec(vocab_list, test_two))
    print('the result is: {}'.format(classifyNaiveBayes(test_two_doc, p0V, p1V, p_abusive)))


# --------项目案例2: 使用朴素贝叶斯过滤垃圾邮件--------------

def textParse(bigString):
    """
    这里就是做词划分
    :param bigString:某个被拼接后的字符串
    :return:全部是小写的word列表，去掉少于 2 个字符的字符串
    """
    import re
    # 其实这里比较推荐用　\W+ 代替 \W*，
    # 因为 \W*会match empty patten，在py3.5+之后就会出现什么问题，推荐自己修改尝试一下，可能就会re.split理解更深了
    listOfTokens=re.split(r'\W+',bigString)
    return [tok.lower() for tok in listOfTokens if len(tok)>2]

def spamTest():
    """
    对贝叶斯垃圾邮件分类器进行自动化处理。
    :return:
    """
    docList=[]
    classList=[]
    fullText=[]
    for i in range(1,26):
        # 添加垃圾邮件信息
        # 这里需要做一个说明，为什么我会使用try except 来做
        # 因为我们其中有几个文件的编码格式是 windows 1252　（spam: 17.txt, ham: 6.txt...)
        # 这里其实还可以 :
        # import os
        # 然后检查 os.system(' file {}.txt'.format(i))，看一下返回的是什么
        # 如果正常能读返回的都是：　ASCII text
        # 对于except需要处理的都是返回： Non-ISO extended-ASCII text, with very long lines
        try:
            wordList=textParse(open('./db/4.NaiveBayes/email/spam/%d.txt'%i).read())
        except:
            wordList = textParse(open('./db/4.NaiveBayes/email/spam/%d.txt' % i,encoding='Windows 1252').read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)

        try:
            wordList=textParse(open('./db/4.NaiveBayes/email/ham/%d.txt'%i).read())
        except:
            wordList = textParse(open('./db/4.NaiveBayes/email/ham/%d.txt' % i,encoding='Windows 1252').read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)

    # 创建词汇表
    vocabList=createVocabList(docList)

    trainingSet=range(50)
    testSet=[]
    for i in range(10):
        randIndex=int(np.random.uniform(0,len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del (list(trainingSet)[randIndex])
    trainMat=[];trainClasses=[]
    for docIndex in trainingSet:
        trainMat.append(bagOfWords2VecMN(vocabList,docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V,p1V,pSpam=trainNaiveBayes(np.array(trainMat),np.array(trainClasses))
    errorCount=0
    for docIndex in testSet:
        wordVector=bagOfWords2VecMN(vocabList,docList[docIndex])
        if classifyNaiveBayes(np.array(wordVector),p0V,p1V,pSpam)!=classList[docIndex]:
            errorCount+=1
    print('the error rate is:',float(errorCount)/len(testSet))

def calcMostFreq(vocabList,fullText):
    '''
    RSS源分类器及高频词去除函数
    :param vocabList:
    :param fullText:
    :return:
    '''
    import operator
    freqDict={}
    for token in vocabList:
        freqDict[token]=fullText.count(token)
    sortedFreq=sorted(freqDict.items(),key=operator.itemgetter(1),reverse=True)
    return sortedFreq[:30]

def localWords(feed1,feed0):
    # import feedparser # 其实呢，这一行没用到，最好删了
    # 下面操作和上面那个 spam_test函数基本一样，理解了一个，两个都ok
    doc_list = []
    class_list = []
    full_text = []
    # 找出两个中最小的一个
    min_len = min(len(feed0), len(feed1))
    for i in range(min_len):
        # 类别　１
        word_list = textParse(feed1['entries'][i]['summary'])
        doc_list.append(word_list)
        full_text.extend(word_list)
        class_list.append(1)
        # 类别　０
        word_list = textParse(feed0['entries'][i]['summary'])
        doc_list.append(word_list)
        full_text.extend(word_list)
        class_list.append(0)
    vocab_list = createVocabList(doc_list)
    # 去掉高频词
    top30words = calcMostFreq(vocab_list, full_text)
    for pair in top30words:
        if pair[0] in vocab_list:
            vocab_list.remove(pair[0])
    # 获取训练数据和测试数据

    import random
    # 生成随机取10个数, 为了避免警告将每个数都转换为整型
    test_set = [int(num) for num in random.sample(range(2 * min_len), 20)]
    # 并在原来的training_set中去掉这10个数
    training_set = list(set(range(2 * min_len)) - set(test_set))

    # 把这些训练集和测试集变成向量的形式
    training_mat = []
    training_class = []
    for doc_index in training_set:
        training_mat.append(bagOfWords2VecMN(vocab_list, doc_list[doc_index]))
        training_class.append(class_list[doc_index])
    p0v, p1v, p_spam = trainNaiveBayes(
        np.array(training_mat),
        np.array(training_class)
    )
    error_count = 0
    for doc_index in test_set:
        word_vec = bagOfWords2VecMN(vocab_list, doc_list[doc_index])
        if classifyNaiveBayes(
                np.array(word_vec),
                p0v,
                p1v,
                p_spam
        ) != class_list[doc_index]:
            error_count += 1
    print("the error rate is {}".format(error_count / len(test_set)))
    return vocab_list, p0v, p1v

def test_rss():
    import feedparser
    ny = feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
    sf = feedparser.parse('http://sfbay.craigslist.org/stp/index.rss')
    vocab_list, p_sf, p_nf = localWords(ny, sf)

def get_top_words():
    import feedparser
    ny = feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
    sf = feedparser.parse('http://sfbay.craigslist.org/stp/index.rss')
    vocab_list, p_sf, p_ny = localWords(ny, sf)
    top_ny = []
    top_sf = []
    for i in range(len(p_sf)):
        if p_sf[i] > -6.0:
            top_sf.append((vocab_list[i], p_sf[i]))
        if p_ny[i] > -6.0:
            top_ny.append((vocab_list[i], p_ny[i]))
    sorted_sf = sorted(top_sf, key=lambda pair: pair[1], reverse=True)
    sorted_ny = sorted(top_ny, key=lambda pair: pair[1], reverse=True)
    print('\n----------- this is SF ---------------\n')
    for item in sorted_sf:
        print(item[0])
    print('\n----------- this is NY ---------------\n')
    for item in sorted_ny:
        print(item[0])

if __name__ == '__main__':
    testingNaiveBayes()
    # spamTest()
    # test_rss()
    # get_top_words()