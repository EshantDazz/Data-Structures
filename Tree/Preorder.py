class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

def preorder_traversal(root):
  if root:
    print(root.value)
    preorder_traversal(root.left)
    preorder_traversal(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

preorder_traversal(root)