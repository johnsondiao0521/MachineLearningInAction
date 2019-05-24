#encoding:utf-8

class Deque(object):
    '''
    双端队列，是一种具有队列和栈的性质的数据结构
    双端队列中的元素可以从两端弹出，其限定插入和删除操作在表的两端进行。双端队列可以在队列任意一端入队和出队。
    '''
    def __init__(self):
        self.__list=[]

    def add_front(self,item):
        '''
        从队头加入一个item元素
        :param item:
        :return:
        '''
        self.__list.insert(0,item)


    def add_rear(self,item):
        '''从队尾加入一个item元素'''
        self.__list.append(item)

    def remove_front(self):
        '''从队头删除一个item元素'''
        return self.__list.pop(0)

    def remove_rear(self):
        '''从队尾删除一个item元素'''
        return self.__list.pop()

    def is_empty(self):
        '''判断双端队列是否为空'''

    def size(self):
        '''返回队列的大小'''
        return len(self.__list)

if __name__ == '__main__':
    deque = Deque()
    deque.add_front(1)
    deque.add_front(2)
    deque.add_rear(3)
    deque.add_rear(4)
    print(deque.size())
    print(deque.remove_front())
    print(deque.remove_front())
    print(deque.remove_front())
    print(deque.remove_front())