#encoding:utf-8

class Queue(object):
    '''
    队列（queue）是只允许在一端进行插入操作，而在另一端进行删除操作的线性表。
    允许插入的一端为队尾，允许删除的一端为堆对头。队列不允许在中间部位进行操作。
    '''
    def __init__(self):
        self.__list=[]

    def enqueue(self,item):
        '''
        往队列中添加一个item元素
        :param item:
        :return:
        '''
        self.__list.append(item)

    def dequeue(self):
        '''
        从队列头部删除一个元素
        :return:
        '''
        return self.__list.pop(0)

    def is_empty(self):
        '''
        判断一个队列是否为空
        :return:
        '''
        return self.__list==[]

    def size(self):
        '''
        返回队列的大小
        :return:
        '''
        return len(self.__list)



if __name__ == '__main__':
    q=Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

