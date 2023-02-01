#Used In
'''
1. Heap Sort
2. Used to implement Priority Queue
3. Two types:
    a) Min Heap(HIghest priority to the lowest value)
    b) Max Heap(Highest priority to the maximum value)
'''


#Complete Binary Tree
'''
When all the nodes are filled from top to bottom and most importantly left to right if the last level is not completely
balanced.

'''
#Advantage of complete binary tree as a binary heap
'''
1. THey can be stored as an array.

left(i)=2i+1
right(i)=2i+2

parent(i)=[i-1/2]

2. Items at continuous locations and random access
3. Cache friendly
4. Height of the tree is minimum possible
'''

class Node:
    def __init__(self,k):
        self.left=None
        self.right=None
        self.key=k

