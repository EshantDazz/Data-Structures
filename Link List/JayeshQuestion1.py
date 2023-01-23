class Node1:
    def __init__(self,k):
        self.key=k
        self.next=None

class Node2:
    def __init__(self,k):
        self.key=k
        self.next=None
def printList(head):
    curr=head
    while curr != None:
        print(curr.key,end=' ')
        curr=curr.next

def Add2(head1,head2):
    cur1=head1
    cur2=head2
    l=[]
    while cur1 and cur2:
        s=cur1.key+cur2.key
        cur1=cur1.next
        cur2=cur2.next
        l.append(s)
    print(l)
head1=None
head2=None
head1=Node1(713)
head1.next=Node1(217)
head1.next.next=Node1(3)
printList(head1)
print()
head2=Node2(100)
head2.next=Node2(300)
head2.next.next=Node2(500)
printList(head2)
print()
Add2(head1,head2)