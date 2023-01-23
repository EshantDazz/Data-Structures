class Node:
    def __init__(self,k):
        self.key=k
        self.next=None

def printList(head):
    curr=head
    while curr != None:
        print(curr.key,end=' ')
        curr=curr.next

def delLast(head):
    if head==None:
        return None
    if head.next==None:
        return None
    cur=head
    while cur.next.next!=None:
        cur=cur.next
    cur.next=None
    return head
head=None
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
printList(head)
print()
head=delLast(head)
printList(head)