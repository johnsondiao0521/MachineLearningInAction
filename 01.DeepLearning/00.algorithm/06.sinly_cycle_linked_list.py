#encoding:utf-8

'''
单链表的一个变形是单向循环链表，链表中最后一个节点的next域不再为None，而是指向链表的头节点。
'''

class Node(object):
    '''节点'''
    def __init__(self,item):
        self._item=item
        self._next=None


class SinCyclLinkedList(object):
    '''单向循环链表'''
    def __init__(self):
        self._head=None

    def is_empty(self):
        '''判断链表是否为空'''
        return self._head==None

    def length(self):
        '''返回链表的长度'''
        # 如果链表为空，返回长度0
        if self.is_empty():
            return 0
        cur=self._head
        count=1
        while cur._next!=self._head:
            cur=cur._next
            count+=1
        return count

    def travel(self):
        '''遍历链表'''
        cur=self._head
        print(cur._item)
        while cur._next!=self._head:
            cur = cur._next
            print(cur._item)
        print(" ")

    def add(self,item):
        '''在头部添加一个节点'''
        # 创建一个节点
        node=Node(item)
        if self.is_empty():
            self._head=node
            node._next=self._head
        else:
            # 添加的节点指向__head
            node._next=self._head
            # 移到链表尾部，将尾部节点的__next指向node
            cur=self._head
            while cur._next!=self._head:
                cur=cur._next
            cur._next=node
            # __head指向添加node的
            self._head=node

    def append(self,item):
        '''尾部添加节点'''
        node=Node(item)
        if self.is_empty():
            self._head=node
            node._next=self._head
        else:
            cur=self._head
            while cur._next!=self._head:
                cur=cur._next
            cur._next=node
            node._next=self._head

    def insert(self,pos,item):
        '''在指定位置添加节点'''
        if pos<=0:
            self.add(item)
        elif pos>(self.length()-1):
            self.append(item)
        else:
            node=Node(item)
            cur=self._head
            count=0
            while count<(pos-1):
                cur=cur._next
                count+=1
            node._next=cur._next
            cur._next=node

    def remove(self,item):
        '''删除一个节点'''
        if self.is_empty():
            return

        cur=self._head
        pre=None
        # 若头节点的元素就是要查找的元素item
        if cur._item==item:
            if cur._next!=self._head:
                while cur._next != self._head:
                    cur = cur._next
                cur._next = self._head._next
                self._head = self._head._next
            else:
                self._head=None
        else:
            pre = self._head
            # 第一个节点不是要删除的
            while cur._next != self._head:
                # 找到了要删除的元素
                if cur._item == item:
                    # 删除
                    pre._next = cur.next
                    return
                else:
                    pre = cur
                    cur = cur._next
            # cur 指向尾节点
            if cur._item == item:
                # 尾部删除
                pre._next = cur._next
    def search(self,item):
        '''查找节点是否存在'''
        if self.is_empty():
            return False
        cur=self._head
        if cur._item==item:
            return True
        while cur._next!=self._head:
            cur=cur._next
            if cur._item==item:
                return True
        return False



if __name__ == '__main__':
    scl=SinCyclLinkedList()
    scl.add(1)
    scl.add(2)
    scl.append(4)
    #print(scl.length())
    scl.travel()
    print(" ")
    scl.remove(4)
    scl.travel()
    print(scl.search(2))
    print(scl.search(3))









