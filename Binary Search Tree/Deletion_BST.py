'''
1. We can delete element having 1 or no children easily
2. If a node has 2 children both non empty then we can replace with the closest number to the deleted element
'''

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def inorder_traversal(root):
  if root:
    inorder_traversal(root.left)
    print(root.key)
    inorder_traversal(root.right)

def getSucc(cur,key):
    while cur.left!=None:
        cur=cur.left
    return cur.key

def deleteNode(root,key):
    if root==None:
        return
    if root.key>key:
        root.left=deleteNode(root.left,key)
    elif root.key<key:
        root.right=deleteNode(root.right,key)
    else:
        if root.left==None:
            return root.right
        elif root.right==None:
            return root.left
        else:
            succ=getSucc(root.right,key)
            root.key=succ
            root.right=deleteNode(root.right,succ)

    return root


root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)

root=deleteNode(root,8)
inorder_traversal(root)

