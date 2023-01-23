#Basic Program
class Node:
    def __init__(self,k):
        self.key=k
        self.next=None

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=head #at this point it is forming a circular link list

#Advantages
'''
1. We can do traversal the whole list from any point
2. Implementation of alforithms like round robin
3. We can insert at the beginning and end by just maintaining one tail pointer
'''

#Disadvantages
'''
Implementation of operations become complex
'''