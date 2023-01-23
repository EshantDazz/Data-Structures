# Keep first pointer at the index from the front where we want to put in the end
#Second one should start from head
#We keep moving 1 at a time and when the second one reaches None the first one will reach at the required position

class Node:
    def __init__(self,k):
        self.key=k
        self.next=None

def print_N_element_from_the_element(head,n):
    if head==None:
        return
    first=head
    for i in range(n):
        if first==None:
            return
        first=first.next
    second=head
    while first!=None:
        second=second.next
        first=first.next
    print(second.key)
head=None
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=Node(50)

print_N_element_from_the_element(head,2)
