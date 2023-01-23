#Constant time
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

def deletFirst(head):
    if head==None:
        return None
    elif head.next==None:
        return None
    else:
        head.key=head.next.key
        head.next=head.next.next
        return head
    
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=head
printCircular(head)
print()
head=deletFirst(head)
printCircular(head)