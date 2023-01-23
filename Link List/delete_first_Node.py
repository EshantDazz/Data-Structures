class Node:
    def __init__(self,k):
        self.key=k
        self.next=None

def printList(head):
    curr=head
    while curr != None:
        print(curr.key,end=' ')
        curr=curr.next
        
def delFirst(head):
    if head==None:
        return None
    return head.next

head=None
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)

printList(head)
head=delFirst(head)
print()
printList(head)