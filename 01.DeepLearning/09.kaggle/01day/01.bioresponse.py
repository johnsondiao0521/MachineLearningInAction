#-*-coding:utf-8-*-

# 用Logistic Regression来搭建模型完成指定的分类任务。

from sklearn.linear_model import LogisticRegression
import csv
import math
import sklearn

def read_data(file_name):
    f = open(file_name)
    f.readline()
    samples = []
    target = []
    for line in f:
        line = line.strip().split(',')
        sample = [float(x) for x in line]
        samples.append(sample)
    return samples

def write_delimited_file(file_path,data,header=None,delimiter=','):
    f_out = open(file_path,'w')
    if header is not None:
        f_out.write(delimiter.join(header)+'\n')
    for line in data:
        if isinstance(line,str):
            f_out.write(line+'\n')
        else:
            f_out.write(delimiter.join(line)+'\n')
    f_out.close()


def train_and_predict():
    # read in the training file
    train = read_data("./data/bioresponse/train.csv")

    print('读取训练数据完毕\n...\n')
    # set the training responses
    target = [x[0] for x in train]
    # set the training features
    train = [x[1:] for x in train]
    # read in the test file
    realtest = read_data("./data/bioresponse/test.csv")
    print('读取待预测数据\n...\n')

    # code for logistic regression
    lr = LogisticRegression()
    lr.fit(train, target)
    print('Logistic Regression训练完毕!\n...\n')
    predicted_probs = lr.predict_proba(realtest)

    # write solutions to file
    predicted_probs = ["%f" % x[1] for x in predicted_probs]
    write_delimited_file("lr_solution.csv", predicted_probs)

    print('Logistic Regression预测完毕! 请提交lr_solution.csv文件到Kaggle')

if __name__ == '__main__':
    train_and_predict()
