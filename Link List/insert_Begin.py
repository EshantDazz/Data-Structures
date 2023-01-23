class Node:
    def __init__(self,k):
        self.key=k
        self.next=None

def printList(head):
    curr=head
    while curr != None:
        print(curr.key,end=' ')
        curr=curr.next

def insert_begin(head,key):
    temp=Node(key)
    temp.next=head
    head=temp
    return head

head=None
head=insert_begin(head,10)
head=insert_begin(head,20)
head=insert_begin(head,45)
printList(head)
 # Time Complexity O(1)
 # Aux Space O(1)