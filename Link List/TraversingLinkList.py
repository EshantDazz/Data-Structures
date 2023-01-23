class Node:
    def __init__(self,k):
        self.key=k
        self.next=None

def printList(head):
    curr=head
    while curr != None:
        print(curr.key,end=' ')
        curr=curr.next

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(45)

printList(head)

#Time Complexity O(n)
#Aux Space :O(1)