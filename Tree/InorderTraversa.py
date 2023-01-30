class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

def inorder_traversal(root):
  if root:
    inorder_traversal(root.left)
    print(root.value)
    inorder_traversal(root.right)

root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.right.left=Node(50)
root.right.right=Node(70)
inorder_traversal(root)