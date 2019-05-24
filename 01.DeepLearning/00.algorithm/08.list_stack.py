#encoding:utf-8

class Stack(object):
    '''
    栈（stack），有些地方称为堆栈，是一种容器，可存入数据元素、访问元素、删除元素，
    它的特点在于只能允许在容器的一端（称为栈顶端指标，英语：top）进行加入数据（英语：push）和输出数据（英语：pop）的运算。
    没有了位置概念，保证任何时候可以访问、删除的元素都是此前最后存入的那个元素，确定了一种默认的访问顺序。
    栈可以用顺序表实现，也可以用链表实现。
    该例子使用顺序表实现
    '''
    def __init__(self):
        self.__list=[]

    def push(self,item):
        '''
        添加一个新的元素item到栈顶
        :param item:
        :return:
        '''
        self.__list.append(item)

    def pop(self):
        '''
        弹出栈顶元素
        :return:
        '''
        if self.__list:
            return self.__list.pop()
        else:
            return None

    def peek(self):
        '''
        返回栈顶元素
        :return:
        '''
        return self.__list[-1]

    def is_empty(self):
        '''
        判断栈是否为空
        :return:
        '''
        return self.__list==[]
    def size(self):
        '''
        返回栈的大小
        :return:
        '''
        return len(self.__list)

if __name__ == '__main__':
    s=Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.is_empty())
    print(s.size())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.is_empty())

