#encoding:utf-8

'''
    基于链表实现的栈
'''

from typing import Optional

class Node(object):
    def __init__(self,data:int,next=None):
        self._data=data
        self._next=next

class LinkedStack(object):
    def __init__(self):
        self._top:None=None
    def push(self,value:int):
        new_top=Node(value)
        new_top._next=self._top
        self._top=new_top

    def pop(self)->Optional[int]:
        if self._top:
            value=self._top._data
            self._top=self._top._next
            return value

    def __repr__(self)->str:
        cur=self._top
        nums=[]
        while cur:
            nums.append(cur._data)
            cur=cur._next
        return " ".join(f"{num}" for num in nums)


if __name__ == '__main__':
    stack = LinkedStack()
    for i in range(9):
        stack.push(i)
    print(stack)
    for _ in range(3):
        stack.pop()
    print(stack)