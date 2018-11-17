#encoding:utf-8

from numpy import *

def loadDataSet(fileName):
    dataMat=[]
    fr=open(fileName)
    for line in fr.readlines():
        curLine=line.strip().split("\t")
        fltLine=[float(x) for x in curLine]
        dataMat.append(fltLine)
    return dataMat

def disEclud(vecA,vecB):
    '''计算向量的欧式距离'''
    return sqrt(sum(power(vecA-vecB,2)))

def randCent(dataSet,k):
    '''
        该函数为给定数据集构建一个包含k个随机质心的集合
        随机质心必须要在整个数据集的边界之内，这可以通过找到数据集每一维的最小和最大值来完成。
        然后生成0到1.0之间的随机数，并通过取值范围和最小值，以便确保随机点在数据的边界之内。
    '''
    # 获取样本数与特征值
    n=shape(dataSet)[1]
    # 初始化质心,创建(k,n)个以零填充的矩阵
    centroids=mat(zeros((k,n)))
    # 循环遍历特征值
    for j in range(n):
        # 计算每一列的最小值
        minJ=min(dataSet[:,j])
        # 计算每一列的范围值
        rangeJ=float(max(dataSet[:,j])-minJ)
        # 计算每一列的质心,并将值赋给centroids
        centroids[:,j]=minJ+rangeJ*random.rand(k,1)
    # 返回质心
    return centroids

def kMeans(dataSet,k,distMeans=disEclud,createCent=randCent):
    '''
        创建K个质心,然后将每个店分配到最近的质心,再重新计算质心。
        这个过程重复数次,直到数据点的簇分配结果不再改变为止
    :param dataSet: 数据集
    :param k: 簇的数目
    :param distMeans: 计算距离
    :param createCent:创建初始质心
    :return:
    '''
    # 获取样本数和特征数
    m,n=shape(dataMat)
    # 初始化一个矩阵来存储每个点的簇分配结果
    # clusterAssment包含两个列:一列记录簇索引值,第二列存储误差(误差是指当前点到簇质心的距离,后面会使用该误差来评价聚类的效果)
    clusterAssment=mat(zeros((m,2)))

    centroids=createCent(dataSet,k)
    clusterChanged=True
    while clusterChanged:
        clusterChanged=False
        for i in range(m):
            minDist=inf;minIndex=-1
            for j in range(k):
                distJI=distMeans(centroids[j,:],dataSet[i,:])
                if distJI<minDist:
                    minDist=distJI;minIndex=j
            if clusterAssment[i,0]!=minIndex:
                clusterChanged=True
            clusterAssment[i,:]=minIndex,minDist**2
        print(centroids)
        for cent in range(k):
            ptsInClust=dataSet[nonzero(clusterAssment[:,0].A==cent)[0]]
            centroids[cent,:]=mean(ptsInClust,axis=0)
    return centroids,clusterAssment

def biKMeans(dataSet,k,distMeans=disEclud):
    m,n=shape(dataSet)
    clusterAssment=mat(zeros((m,2)))
    centroid0=mean(dataSet,axis=0).tolist()[0]
    centList=[centroid0]
    for j in range(m):
        clusterAssment[j,1]=distMeans(mat(centroid0),dataSet[j,:])**2
    while (len(centList)<k):
        lowestSSE=inf
        for i in range(len(centList)):
            ptsInCurrCluster=dataSet[nonzero(clusterAssment[:,0].A==i)[0],:]
            centroidMat,splitClustAss=kMeans(ptsInCurrCluster,2,distMeans)
            sseSplit=sum(splitClustAss[:,1])

if __name__ == '__main__':
    dataMat=mat(loadDataSet("10.testSet.txt"))

    minOfMat0 = min(dataMat[:, 0])
    print("minOfMat0:", minOfMat0)
    minOfMat1=min(dataMat[:,1])
    print("minOfMat1",minOfMat1)

    maxOfMat0 = max(dataMat[:, 0])
    print("maxOfMat0:", maxOfMat0)
    maxOfMat1 = max(dataMat[:, 1])
    print("maxOfMat1", maxOfMat1)

    centroids=randCent(dataMat,3)
    print("centroids:",centroids)

    print("dataMat[0]:",dataMat[0])
    print("dataMat[1]:",dataMat[1])
    disEclud=disEclud(dataMat[0],dataMat[1])
    print("disEclud:",disEclud)
    myCentroids,clustAssing=kMeans(dataMat,4)
    print("myCentroids:",myCentroids)
    print("clustAssing:",clustAssing)


