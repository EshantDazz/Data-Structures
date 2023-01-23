class Node:
    def __init__(self,k):
        self.key=k
        self.next=None

def printCircular(head):
    while head==None:
        return
    print(head.key,end=' ')
    cur=head.next
    while(cur!=head):
        print(cur.key,end=' ')
        cur=cur.next

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=head
printCircular(head)