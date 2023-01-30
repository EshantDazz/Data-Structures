#if root==None then that means it is an empty binary tree
class Node:
    def __init__(self,k):
        self.left=None
        self.right=None
        self.key=k


root=Node(10)
root.right=Node(20)
root.left=Node(30)
root.left.left=Node(40)

