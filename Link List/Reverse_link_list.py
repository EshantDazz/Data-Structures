#We can do it using the stack method
class Node:
    def __init__(self,k):
        self.key=k
        self.next=None

def printList(head):
    curr=head
    while curr != None:
        print(curr.key,end=' ')
        curr=curr.next

def reverseList(head):
    cur=head
    prev=None
    while cur:
        next=cur.next
        cur.next=prev
        prev=cur
        cur=next
    return prev

head=None
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
printList(head)
print()
head=reverseList(head)
printList(head)
