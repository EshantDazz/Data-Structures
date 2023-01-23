# In the case of 2 middle nodes we print the second middle node
class Node:
    def __init__(self,k):
        self.key=k
        self.next=None

def Middle1(head):
    if head==None:
        return 
    count =0
    cur=head
    while cur:
        cur=cur.next
        count+=1
    cur=head
    for i in range(count//2):
        cur=cur.next
    print("First Function.  ",cur.key)

def Middle2(head):
    if head==None:
        return
    slow=head
    fast=head
    while fast!=None and fast.next!=None:
        slow=slow.next
        fast=fast.next.next
    print("Second Function   ",slow.key)

head=None
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=Node(50)
Middle1(head)
print()
Middle2(head)
