#encoding:utf-8

'''
双链表：每个节点有两个链接：一个指向前一个节点，当此节点为第一个节点时，指向空值；而另一个指向下一个节点，当此节点为最后一个节点时，指向空值。
'''

class Node(object):
    '''双向链表节点'''
    def __init__(self,item):
        self._item=item
        self._next=None
        self._prev=None


class DoubleLinkList(object):
    '''双向链表'''
    def __init__(self):
        self._head=None

    def is_empty(self):
        '''判断链表是否为空'''
        return self._head==None

    def length(self):
        """返回链表的长度"""
        cur=self._head
        count=0
        while cur!=None:
            cur=cur._next
            count+=1
        return count

    def travel(self):
        '''遍历链表'''
        cur=self._head
        while cur!=None:
            print(cur._item)
            cur=cur._next
        print(" ")

    def add(self,item):
        '''头部插入元素'''
        node=Node(item)
        if self.is_empty():
            # 如果是空链表，将_head指向node
            self._head=node
        else:
            node._next=self._head
            self._head._prev=node
            self._head=node

    def append(self,item):
        '''尾部插入元素'''
        node=Node(item)
        if self.is_empty():
            self._head=node
        else:
            # 移动到链表尾部
            cur=self._head
            while cur._next!=None:
                cur=cur._next
            cur._next=node
            node._prev=cur

    def search(self,item):
        '''查找元素是否存在'''
        cur=self._head
        while cur!=None:
            if cur._item==item:
                return True
            cur=cur._next
        return False

    def insert(self,pos,item):
        '''在指定位置添加节点'''
        if pos<=0:
            self.add(item)
        elif pos>self.length()-1:
            self.append(item)
        else:
            node=Node(item)
            cur=self._head
            count=0
            while count<(pos-1):
                count+=1
                cur=cur._next
            node._next=cur._next
            cur._next._prev=node
            node._prev=cur
            cur._next=node

    def remove(self,item):
        '''删除元素'''
        if self.is_empty():
            return
        else:
            cur = self._head
            if cur._item == item:
                # 如果首节点的元素即是要删除的元素
                if cur._next == None:
                    # 如果链表只有这一个节点
                    self._head = None
                else:
                    # 将第二个节点的prev设置为None
                    cur._next._prev = None
                    # 将_head指向第二个节点
                    self._head = cur._next
                return
            while cur != None:
                if cur._item == item:
                    # 将cur的前一个节点的next指向cur的后一个节点
                    cur._prev._next = cur._next
                    # 将cur的后一个节点的prev指向cur的前一个节点
                    cur._next._prev = cur._prev
                    break
                cur = cur._next



if __name__ == '__main__':
    dll=DoubleLinkList()
    dll.add(1)
    dll.add(2)
    dll.add(3)
    dll.append(4)
    dll.travel()
    print(dll.length())
    print(dll.search(4))
    print(dll.search(5))
    dll.insert(2,8)
    dll.insert(2,8)
    dll.travel()
    dll.remove(8)
    dll.travel()
