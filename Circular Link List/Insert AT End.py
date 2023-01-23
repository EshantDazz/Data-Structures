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
def InsertEnd(head,x):
    temp=Node(x)
    if temp==None:
        temp.next=temp
        return temp
    else:
        temp.next=head.next
        head.next=temp
        head.key,temp.key=temp.key,head.key
        return temp

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=head
printCircular(head)
print()
head=InsertEnd(head,100)
printCircular(head)