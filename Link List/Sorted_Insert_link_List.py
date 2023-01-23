#We need to insert the link List in such a way that after the insertion the Link List remains sorted
class Node:
    def __init__(self,k):
        self.key=k
        self.next=None

def printList(head):
    curr=head
    while curr != None:
        print(curr.key,end=' ')
        curr=curr.next

def insert_Sorted(head,x):
    temp=Node(x)
    if head==None:
        return head
    elif x<head.key:
        temp.next=head 
        return temp
    else:
        cur=head
        while cur.next!=None and cur.next.key<x:
            cur=cur.next
        temp.next=cur.next
        cur.next=temp
        return head
    
head=None
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)

head=insert_Sorted(head,25)
printList(head)