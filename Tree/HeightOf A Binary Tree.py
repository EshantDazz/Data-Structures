class Node:
    def __init__(self,k):
        self.left=None
        self.right=None
        self.key=k

def height(root):
    if root is None:
        return 0
    lh=height(root.left)
    rh=height(root.right)
    return max(lh,rh)+1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(height(root))
'''This program creates a binary tree with the following structure:

markdown
Copy code
    1
   / \
  2   3
 / \
4   5
and calculates its height, printing the value 3.'''




