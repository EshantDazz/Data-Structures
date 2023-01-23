class Node:
    def __init__(self,k):
        self.key=k
        self.next=None

def Traversal(head):
    cur=head
    while cur:
        print(cur.key,end=' ')
        cur=cur.next

#Remove from a sorted Link List
def removeDuplicates(head):
    cur=head
    while(cur!=None and cur.next!=None):
        if(cur.key==cur.next.key):
            cur.next=cur.next.next
        else:
            cur=cur.next
    return head


head=Node(20)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=Node(50)
head.next.next.next.next.next=Node(50)

Traversal(head)
print()
head=removeDuplicates(head)
Traversal(head)