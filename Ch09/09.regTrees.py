#encoding:utf-8


from numpy import *



def loadDataSet(fileName):
    dataMat=[]
    fr=open(fileName)
    for line in fr.readlines():
        curLine=line.strip().split('\t')
        # 将每行转换成浮点数
        fltLine = [float(x) for x in curLine]
        dataMat.append(fltLine)
    return dataMat

def binSplitDataSet(dataSet,feature,value):
    '''
    binSplitDataSet(将数据集，按照feature列的value进行 二元切分)
    :param dataSet: 数据集
    :param feature: 待切分的特征列
    :param value: 待切分的特征列的值
    :return: mat0 小于等于 value 的数据集在左边
             mat1 大于 value 的数据集在右边
    '''
    mat0=dataSet[nonzero(dataSet[:,feature]>value)[0],:][0]
    mat1=dataSet[nonzero(dataSet[:,feature<=value])[0],:][0]
    return mat0,mat1

def regLeaf(dataSet):
    '''
    返回每一个叶子结点的均值
    :param dataSet:
    :return:
    '''
    return mean(dataSet[:,-1])
def regErr(dataSet):
    '''
     计算总方差=方差*样本数
    :param dataSet:
    :return:
    '''
    return var(dataSet[:,-1])*shape(dataSet)[0]

def chooseBestSplit(dataSet,leafType=regLeaf,errType=regErr,ops=(1,4)):
    tolS=ops[0];tolN=ops[1]
    if len(set(dataSet[:,-1].T.tolist()[0]))==1:
        return None,leafType(dataSet)
    m,n=shape(dataSet)
    S=errType(dataSet)
    bestS=inf;bestIndex=0;bestValue=0
    for featIndex in range(n-1):
        for splitVal in set(dataSet[:,featIndex]):
            mat0,mat1=binSplitDataSet(dataSet,featIndex,splitVal)
            if (shape(mat0)[0] < tolN) or (shape(mat1)[0] < tolS):continue
            newS=errType(mat0) + errType(mat1)
            if newS < bestS:
                bestIndex=featIndex
                bestValue=splitVal
                bestS=newS
    if (S-bestS) < tolS:
        return None,leafType(dataSet)
    if (shape(mat0)[0] < tolN) or (shape(mat1)[0] < tolN):
        return None,leafType(dataSet)
    return bestIndex,bestValue

def isTree(obj):
    return (type(obj).__name__ == 'dict')

def getMean(tree):
    if isTree(tree['right']):
        tree['right']=getMean(tree['right'])
    if isTree(tree['left']):
        tree['left']=getMean(tree['left'])
    return (tree['right']+tree['left']) / 2.0

def prune(tree,testData):
    if shape(testData)[0]==0:
        return getMean(tree)
    if (isTree(tree['right'])) or isTree(tree['left']):
        lSet,rSet=binSplitDataSet(test,tree['spInd'],tree['spVal'])
        errorNoMerge=sum(power(lSet[:,-1]-tree['left'],2))+sum(power(rSet[:,-1]-tree['right'],2))
        treeMean=(tree['left']+tree['right'])/2.0
        errorMerge=sum(power(testData[:,-1]-treeMean,2))
        if errorMerge<errorNoMerge:
            print("merging")
            return treeMean
        else:
            return tree
    else:
        return tree

def createTree(dataSet,leafType=regLeaf,errType=regErr,ops=(1,4)):
    feat,val=chooseBestSplit(dataSet,leafType,errType,ops)
    if feat==None:return val
    retTree={}
    retTree['spInd']=feat
    retTree['spVal']=val
    lSet,rSet=binSplitDataSet(dataSet,feat,val)
    retTree['left']=createTree(dataSet,leafType,errType,ops)
    retTree['right']=createTree(dataSet,leafType,errType,ops)
    return retTree

def linearSolve(dataSet):
    m,n=shape(dataSet)
    X=mat(ones((m,n)));Y=mat(ones((m,1)))
    X[:,1:n]=dataSet[:,0:n-1];Y=dataSet[:,-1]
    #X[:, 1:n] = dataSet[:, 0:n - 1]
    #Y = dataSet[:, -1]
    xTx=X.T*X
    if linalg.det(xTx)==0.0:
        raise NameError("This matrix is singular,cannot do inverse,try increasing the second value of ops")
    ws=xTx.I*(X.T*Y)
    return ws,X,Y

def modelLeaf(dataSet):
    ws,X,Y=linearSolve(dataSet)
    return ws

def modelErr(dataSet):
    ws,X,Y=linearSolve(dataSet)
    yHat=X*ws
    return sum(power(Y-yHat),2)

def regTreeEval(model,inDat):
    return float(model)

def modelTreeEval(model,inDat):
    n=shape(inDat)[1]
    X=mat(ones((1,n+1)))
    X[:,1:n+1]=inDat
    return float(X*model)

def treeForeCast(tree,inData,modelEval=regTreeEval):
    if not isTree(tree):return modelEval(tree,inData)
    if inData[tree['spInd']]>tree['spVal']:
        if isTree(tree['left']):
            return treeForeCast(tree['left'],inData,modelEval)
        else:
            return modelEval(tree['left'],inData)
    else:
        if isTree(tree['right']):
            return treeForeCast(tree['right'],inData,modelEval)
        else:
            return modelEval(tree['right'],inData)

def createForeCast(tree,testData,modelEval=regTreeEval):
    m=len(testData)
    yHat=mat(zeros((m,1)))
    for i in range(m):
        yHat[i,0]=treeForeCast(tree,mat(testData[i]),modelEval)
    return yHat

def test2():
    trainMat=mat(loadDataSet("09.bikeSpeedVsIq_train.txt"))
    testMat=mat(loadDataSet("09.bikeSpeedVsIq_test.txt"))
    myTree=createTree(trainMat,ops=(1,20))
    yHat=createForeCast(myTree,testMat[:,0])
    corrcoef(yHat,testMat[:,-1],rowvar=0)[0,1]

def test():
    myMat2=mat(loadDataSet("09.ex2.txt"))
    createTree(myMat2,modelLeaf,modelErr,(1,10))




if __name__ == '__main__':
    #test2()
    import _tkinter
    from tkinter import *
    root=Tk()
    myLabel=Label(root,text="hello world")
    myLabel.grid()
    root.mainloop()



