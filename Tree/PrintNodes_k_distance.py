class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

def print_nodes_at_distance_k(root, k):
  if root is None:
    return
  if k == 0:
    print(root.value)
    return
  print_nodes_at_distance_k(root.left, k - 1)
  print_nodes_at_distance_k(root.right, k - 1)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print_nodes_at_distance_k(root, 2)
'''This program creates a binary tree with the following structure:


    1
   / \
  2   3
 / \
4   5
and prints the nodes at distance 2 from the root, printing the values 2 3.'''