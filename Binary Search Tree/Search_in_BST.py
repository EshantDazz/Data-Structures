class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def searchBST(node,key):
    while node!=None:
        if node.key==key:
            return True
        elif node.key>key:
            node=node.left
        else:
            node=node.right
    return False

root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)

b=searchBST(root,6)
if b:
    print("Key is present")
else:
    print("Element is not present")