#encoding:utf-8

import numpy as np


def loadDataSet(fileName,delim="\t"):
    fr=open(fileName)
    stringArr=[line.strip().split(delim) for line in fr.readlines()]
    # 注意这里和python2的区别，需要在map函数外加一个list（），否则显示结果为 map at 0x3fed1d0
    datArr=[list(map(float,line)) for line in stringArr]
    return np.mat(datArr)

def pca(dataMat,topNfeat=9999999):
    """

    :param dataMat:原数据集矩阵
    :param topNfeat:应用的N个特征
    :return:
        lowDDataMat:降维后数据集
        reconMat:新的数据集空间
    """
    # 计算每一列的均值
    meanVals = np.mean(dataMat, axis=0)

    # 每个向量同时都减去 均值
    meanRemoved = dataMat - meanVals

    # cov协方差=[(x1-x均值)*(y1-y均值)+(x2-x均值)*(y2-y均值)+...+(xn-x均值)*(yn-y均值)+]/(n-1)
    covMat = np.cov(meanRemoved, rowvar=0)

    # eigVals为特征值， eigVects为特征向量
    eigVals, eigVects = np.linalg.eig(np.mat(covMat))
    eigValInd = np.argsort(eigVals)
    eigValInd = eigValInd[:-(topNfeat + 1):-1]  # cut off unwanted dimensions
    redEigVects = eigVects[:, eigValInd]  # reorganize eig vects largest to smallest
    lowDDataMat = meanRemoved * redEigVects  # transform data into new dimensions
    reconMat = (lowDDataMat * redEigVects.T) + meanVals
    return lowDDataMat, reconMat

def replaceNanWithMean():
    datMat = loadDataSet('./db/13.PCA/secom.data', ' ')
    numFeat = np.shape(datMat)[1]
    for i in range(numFeat):
        meanVal = np.mean(datMat[np.nonzero(~np.isnan(datMat[:,i].A))[0],i]) #values that are not NaN (a number)
        datMat[np.nonzero(np.isnan(datMat[:,i].A))[0],i] = meanVal  #set NaN values to mean
    return datMat


if __name__ == '__main__':
    dataMat=loadDataSet("./db/13.PCA/testSet.txt")
    lowDMat,reconMat=pca(dataMat,1)
    import matplotlib
    import matplotlib.pyplot as plt
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.scatter(dataMat[:,0].flatten().A[0],dataMat[:,1].flatten().A[0],marker='^',s=9)
    ax.scatter(reconMat[:, 0].flatten().A[0], reconMat[:,1].flatten().A[0], marker='o', s=5,c='red')
    plt.show()

    dataMat=replaceNanWithMean()
    meanVals=np.mean(dataMat,axis=0)
    meanRemoved=dataMat-meanVals
    covMat=np.cov(meanRemoved,rowvar=0)
    eightVals,eightVects=np.linalg.eig(np.mat(covMat))
    print(eightVals)