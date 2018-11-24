#encoding:utf-8

from numpy import *

class treeNode:
    def __init__(self,nameValue,numOccur,parentNode):
        self.name=nameValue # 节点名称
        self.count=numOccur # 节点出现次数
        self.nodeLink=None # 不同项集的相同项通过nodeLink连接在一起
        self.parent=parentNode # 指向父节点
        self.children={} # 存储叶子节点

    def inc(self,numOccur):
        """inc(对count变量增加给定值)"""
        self.count=numOccur

    def disp(self,ind=1):
        """disp(用于将树以文本形式显示)"""
        print(" "*ind,self.name," ",self.count)
        for child in self.children.values():
            child.disp(ind+1)


def updateHeader(nodeToTest, targetNode):
    '''
        updateHeader(更新头指针，建立相同元素之间的关系，例如： 左边的r指向右边的r值，就是后出现的相同元素 指向 已经出现的元素)

        从头指针的nodeLink开始，一直沿着nodeLink直到到达链表末尾。这就是链表。
        性能：如果链表很长可能会遇到迭代调用的次数限制。
    :param nodeToTest:满足minSup {所有的元素+(value, treeNode)}
    :param targetNode:Tree对象的子节点
    :return:
    '''
    # 建立相同元素之间的关系，例如： 左边的r指向右边的r值
    while (nodeToTest.nodeLink is not None):
        nodeToTest = nodeToTest.nodeLink
    nodeToTest.nodeLink = targetNode

def updateTree(items,inTree,headerTable,count):
    '''
    updateTree(更新FP-tree，第二次遍历)
     # 针对每一行的数据
    # 最大的key,  添加

    :param items:满足minSup 排序后的元素key的数组（大到小的排序）
    :param inTree:空的Tree对象
    :param headerTable:满足minSup{所有的元素+(value,treeNode)}
    :param count:原数据集中每一组key出现的次数
    :return:
    '''
    # 取出 元素 出现次数最高的
    # 如果该元素在 inTree.children 这个字典中，就进行累加
    # 如果该元素不存在 就 inTree.children 字典中新增key，value为初始化的 treeNode 对象
    if items[0] in inTree.children:
        # 更新 最大元素，对应的 treeNode 对象的count进行叠加
        inTree.children[items[0]].inc(count)
    else:
        # 如果不存在子节点，我们为该inTree添加子节点
        inTree.children[items[0]]=treeNode(items[0],count,inTree)
        # 如果满足minSup的dist字典的value值第二位为null， 我们就设置该元素为 本节点对应的tree节点
        # 如果元素第二位不为null，我们就更新header节点
        if headerTable[items[0]][1] is None:
            headerTable[items[0]][1]=inTree.children[items[0]]
        else:
            # 本质上是修改headerTable的key对应的Tree，的nodeLink值
            updateHeader(headerTable[items[0]][1],inTree.children[items[0]])

    if len(items)>1:
        # 递归的调用，在items[0]的基础上，添加item0[1]做子节点， count只要循环的进行累计加和而已，统计出节点的最后的统计值。
        updateTree(items[1::],inTree.children[items[0]],headerTable,count)

def createTree(dataSet, minSup=1):
    """createTree(生成FP-tree)

    Args:
        dataSet  dist{行：出现次数}的样本数据
        minSup   最小的支持度
    Returns:
        retTree  FP-tree
        headerTable 满足minSup {所有的元素+(value, treeNode)}
    """
    # 支持度>=minSup的dist{所有元素：出现的次数}
    headerTable = {}
    # 循环 dist{行：出现次数}的样本数据
    for trans in dataSet:
        # 对所有的行进行循环，得到行里面的所有元素
        # 统计每一行中，每个元素出现的总次数
        for item in trans:
            # 例如： {'ababa': 3}  count(a)=3+3+3=9   count(b)=3+3=6
            headerTable[item] = headerTable.get(item, 0) + dataSet[trans]
    # 删除 headerTable中，元素次数<最小支持度的元素
    for k in list(headerTable.keys()):  # python3中.keys()返回的是迭代器不是list,不能在遍历时对其改变。
        if headerTable[k] < minSup:
            del(headerTable[k])

    # 满足minSup: set(各元素集合)
    freqItemSet = set(headerTable.keys())
    # 如果不存在，直接返回None
    if len(freqItemSet) == 0:
        return None, None
    for k in headerTable:
        # 格式化： dist{元素key: [元素次数, None]}
        headerTable[k] = [headerTable[k], None]

    # create tree
    retTree = treeNode('Null Set', 1, None)
    # 循环 dist{行：出现次数}的样本数据
    for tranSet, count in dataSet.items():
        # print('tranSet, count=', tranSet, count)
        # localD = dist{元素key: 元素总出现次数}
        localD = {}
        for item in tranSet:
            # 判断是否在满足minSup的集合中
            if item in freqItemSet:
                # print('headerTable[item][0]=', headerTable[item][0], headerTable[item])
                localD[item] = headerTable[item][0]
        # print('localD=', localD)
        # 对每一行的key 进行排序，然后开始往树添加枝丫，直到丰满
        # 第二次，如果在同一个排名下出现，那么就对该枝丫的值进行追加，继续递归调用！
        if len(localD) > 0:
            # p=key,value; 所以是通过value值的大小，进行从大到小进行排序
            # orderedItems 表示取出元组的key值，也就是字母本身，但是字母本身是大到小的顺序
            orderedItems = [v[0] for v in sorted(localD.items(), key=lambda p: p[1], reverse=True)]
            # print 'orderedItems=', orderedItems, 'headerTable', headerTable, '\n\n\n'
            # 填充树，通过有序的orderedItems的第一位，进行顺序填充 第一层的子节点。
            updateTree(orderedItems, retTree, headerTable, count)

    return retTree, headerTable

def loadSimpDat():
    simpDat=[['r','z','h','j','p'],
             ['z','y','x','w','v','u','t','s'],
             ['z'],
             ['r','x','n','o','s'],
             ['y','r','x','z','q','t','p'],
             ['y','z','x','e','q','s','t','m']
            ]
    return simpDat

def createInitSet(dataSet):
    retDict={}
    for trans in dataSet:
        retDict[frozenset(trans)]=1
    return retDict


if __name__ == '__main__':
    # 1.
    # rootNode=treeNode("pyramid",9,None)
    # rootNode.children["eye"]=treeNode("eye",13,None)
    # rootNode.children["phoenix"]=treeNode("phoenix",3,None)
    # rootNode.disp()

    # 2.
    simpDat=loadSimpDat()
    initSet=createInitSet(simpDat)
    myFptree,myHeaderTable=createTree(initSet,3)
    myFptree.disp()