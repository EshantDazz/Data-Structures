class Node:
    def __init__(self,k):
        self.left=None
        self.right=None
        self.key=k

def SizeofTree(node):
    if node is None:
        return 0
    else:
        ls=SizeofTree(node.left)
        rs=SizeofTree(node.right)
        return ls+rs+1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

s=SizeofTree(root)
print(s)
'''This program creates a binary tree with the following structure:


    1
   / \
  2   3
 / \
4   5'''