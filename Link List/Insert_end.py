class Node:
    def __init__(self,k):
        self.key=k
        self.next=None

def printList(head):
    curr=head
    while curr != None:
        print(curr.key,end=' ')
        curr=curr.next

def insert_end(head,key):
    if(head==None):
        return Node(key)
    cur=head
    while(cur.next!=None):
        cur=cur.next
    cur.next=Node(key)
    return head

head=None
head=insert_end(head,10)
head=insert_end(head,20)
head=insert_end(head,30)
printList(head)