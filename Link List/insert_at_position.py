

class Node:
    def __init__(self,k):
        self.key=k
        self.next=None

def printList(head):
    curr=head
    while curr != None:
        print(curr.key,end=' ')
        curr=curr.next

def insert_at_position(head,key,pos):
    temp=Node(key)
    if pos==1:
        temp.next=head
        head=temp
        return head
    cur=head
    for i in range(pos-2):
        cur=cur.next
        if(cur==None):
            return head
    temp.next=cur.next
    cur.next=temp
    return head
head=None
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
printList(head)

head=insert_at_position(head,999,2)
print()
printList(head)