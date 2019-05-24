#encoding:utf-8

# 1) 制作词向量，可以使用gensim这个库，也可以直接用现成的
# 2) 词和ID的映射
# 3) 构建RNN网络架构
# 4) 训练我们的模型

# 为了得到词向量，使用TensorFlow的嵌入函数。
# 这个函数有2个参数，一个是嵌入矩阵(词向量矩阵)，
# 另一个是每个词对应的索引。

import numpy as np
import tensorflow as tf

from os import listdir
from os.path import isfile,join

import matplotlib.pyplot as plt

import re

def load_data():
    '''加载wordsList和wordVectors的数据'''
    # 包含400000个单词的python列表
    word_list=np.load("./training_data/wordsList.npy")
    print("Loaded the word list!")
    word_list=word_list.tolist()
    word_list=[word.decode('UTF-8') for word in word_list]
    # 包含所有单词向量400000*50维的嵌入矩阵
    word_vectors=np.load("./training_data/wordVectors.npy")
    print ('Loaded the word vectors!')
    return word_list,word_vectors

def test_baseball(word_list,word_vectors):
    '''
    # 测试baseball的词向量
    :param wordsList:单词列表
    :param wordVectors:词向量矩阵
    :return:
    '''
    baseball_index = word_list.index("baseball")
    print("baseball在词向量矩阵中的位置：",word_vectors[baseball_index])


# 在整个训练集上面构造索引之前，来可视化所拥有的数据类型。
# 这将帮助我们去决定如何设置最大序列长度的最佳值。在前面的例子中，我们设置了最大长度为 10，
# 但这个值在很大程度上取决于你输入的数据。
def show(numWords):
    '''

    :return:
    '''
    plt.hist(numWords,50)
    plt.xlabel('Sequence Length')
    plt.ylabel('Frequency')
    plt.axis([0,1200,0,8000])
    plt.show()
    # 从直方图和句子的平均单词数，我们认为将句子最大长度设置为250是可行的

def length_sentence(wordsList,max_seq_length = 10):
    '''
    输入一个句子，然后构造它的向量表示
    将一句话中的每一个词都转换成一个向量
    :param wordsList: 测试的句子 I thought the movie was incredible and inspiring
    :param maxSeqLength:每个单词的构造向量维度
    :return:
    '''
    seq_length_sentence=np.zeros((max_seq_length),dtype='int32')
    seq_length_sentence[0] = wordsList.index("i")
    seq_length_sentence[1] = wordsList.index("thought")
    seq_length_sentence[2] = wordsList.index("the")
    seq_length_sentence[3] = wordsList.index("movie")
    seq_length_sentence[4] = wordsList.index("was")
    seq_length_sentence[5] = wordsList.index("incredible")
    seq_length_sentence[6] = wordsList.index("and")
    seq_length_sentence[7] = wordsList.index("inspiring")
    #firstSentence[8]  firstSentence[9] 被赋值为0了
    print("seq_length_sentence的shape:",seq_length_sentence.shape)
    # 查看每个单词对应的位置
    print("I thought the movie was incredible and inspiring中每个单词对应的向量：",seq_length_sentence)

    with tf.Session() as sess:
        print("seq_length_sentence经过管道输出：",tf.nn.embedding_lookup(wordVectors,seq_length_sentence).eval())

    return seq_length_sentence

def read_positive_negative():
    positive_files = ['./training_data/positiveReviews/' + f for f in listdir('./training_data/positiveReviews/') if isfile(join('./training_data/positiveReviews/', f))]
    negative_files = ['./training_data/negativeReviews/' + f for f in listdir('./training_data/negativeReviews/') if isfile(join('./training_data/negativeReviews/', f))]
    num_words=[]
    for pf in positive_files:
        with open(pf,'r',encoding='utf-8') as f:
            line=f.read()
            counter=len(line.split())
            num_words.append(counter)
    print("Positive files finished")

    for nf in negative_files:
        with open(nf,'r',encoding='utf-8') as f:
            line=f.read()
            counter=len(line.split())
            num_words.append(counter)
    num_files = len(num_words)
    print('The total number of files is', num_files)
    print('The total number of words in the files is', sum(num_words))
    print('The average number of words in the files is', sum(num_words)/len(num_files))




def clean_sentences(string):
    '''
    清洗句子中的特殊字符
    :param string:句子
    :return:
    '''
    strip_special_chars = re.compile("[^A-Za-z0-9]]+")
    string=string.lower().replace("<br />"," ")
    return re.sub(strip_special_chars,"",string.lower())

def testtt(maxSeqLength,fname,firstSentence):
    firstFile=np.zeros((maxSeqLength),dtype="int32")
    with open(fname) as f:
        indexCounter=0
        line=f.readline()
        cleanedLine=clean_sentences(line)
        split=cleanedLine.split()
        for word in split:
            try:
                firstSentence[indexCounter]=wordsList.index(word)
            except ValueError:
                firstFile[indexCounter]=399999
            indexCounter=indexCounter+1

    print(firstFile)


if __name__ == '__main__':
    # 加载需要测试的句子列表和词向量矩阵
    wordsList,wordVectors=load_data()
    print(len(wordsList))
    print(wordVectors.shape)
    # baseball单词在词向量的位置
    test_baseball(wordsList,wordVectors)
    # I thought the movie was incredible and inspiring 所对应的词向量
    length_sentence(wordsList,maxSeqLength=10)

    # fname = positiveFiles[3]
    # with open(fname) as f:
    #     for lines in f:
    #         print(lines)
    #         break









