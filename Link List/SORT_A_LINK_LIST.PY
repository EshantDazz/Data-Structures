class Node:
    def __init__(self,k):
        self.key=k
        self.next=None
class SortList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def addNone(self,data):
        newNode=Node(data)

        if(self.head==None):
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
    def SortList(self):
        cur=self.head
        index=None
        if cur==None:
            return
        else:
            while(cur!=None):
                index=cur.next
                while(index!=None):
                    if(cur.key>index.key):
                        cur.key,index.key=index.key,cur.key
                    index=index.next
                cur=cur.next
    def display(self):
        cur=self.head
        while cur:
            print(cur.key,end=' ')
            cur=cur.next
        print()
ob=SortList()
ob.addNone(8)
ob.addNone(4)
ob.addNone(3)
ob.addNone(7)
ob.display()
ob.SortList()
ob.display()


