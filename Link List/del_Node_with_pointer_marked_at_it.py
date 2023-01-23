class Node:
    def __init__(self,k):
        self.key=k
        self.next=None

def printList(head):
    curr=head
    while curr != None:
        print(curr.key,end=' ')
        curr=curr.next
def delPointer(ptr):
    temp=ptr.next
    ptr.key=temp.key
    ptr.next=temp.next

head=None
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
delPointer(head.next)
printList(head)