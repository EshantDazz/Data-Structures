import math
class Node:
    def __init__(self,k):
        self.left=None
        self.right=None
        self.key=k
def getMax(node):
    if node is None:
        return -math.inf
    else:
        ls=getMax(node.left)
        rs=getMax(node.right)
        return max(node.key,ls,rs)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(getMax(root))
'''This program creates a binary tree with the following structure:


    1
   / \
  2   3
 / \
4   5'''
