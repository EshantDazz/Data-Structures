'''
Floor in a BST is the largest number smaller or equal to the  number given
'''

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def findFloor(root,x):
    res=None
    while(root!=None):
        if root.key==x:
            return root
        elif x<root.key:
            root=root.left
        else:
            res=root
            root=root.right
    return res

root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)

l=findFloor(root,13)
print(l.key)