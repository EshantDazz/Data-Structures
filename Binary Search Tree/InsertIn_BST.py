class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
'''
1. Any value inserted will go as the leaf node
2. THe root can only be modified in case the tree was empty initially
'''
def inorder_traversal(root):
  if root:
    inorder_traversal(root.left)
    print(root.key)
    inorder_traversal(root.right)

def insert(root,key):
    parent=None
    cur=root
    while(cur!=None):
        parent=cur
        if cur.key==key:
            return root
        elif cur.key>key:
            cur=cur.left
        else:
            cur=cur.right
    if parent==None:
        return Node(key)
    if parent.key>key:
        parent.left=Node(key)
    else:
        parent.right=Node(key)
    return root


root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)

root=insert(root,9)
inorder_traversal(root)
