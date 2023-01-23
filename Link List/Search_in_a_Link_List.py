class Node:
    def __init__(self,k):
        self.key=k
        self.next=None

def search(head,x):
    pos=1
    cur=head
    while cur!=None:
        if cur.key == x:
            return pos
        pos+=1
        cur=cur.next
    return -1


head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(45)
x=270
print(search(head,x))

#Time Complexity --> O(n)
#Aux Space --> O(1)

