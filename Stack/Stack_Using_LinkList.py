
#Implemetaiton of Stack using Link List
import math
class Node:
    def __init__(self,d):
        self.data=d
        self.next=None
class Mystack:
    def __init__(self):
        self.head=None
        self.sz=0
    def push(self,x):
        temp=Node(x)
        temp.next=self.head
        self.head=temp
        self.sz+=1
    def peek(self):
        if not self.head:
            return math.inf
        return self.head.data
    def pop(self):
        if not self.head:
            return math.inf
        res=self.head.data
        self.head=self.head.next
        self.sz-=1
        return res
s=Mystack()
s.push(20)
s.push(45)
print(s.peek())
print(s.pop())
print(s.peek())

