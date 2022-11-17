#Stack in Python
'''
Using List
Using collection.deque -> doubly link list
Using queue.LIFO queue.--> This one we generally don't use in a single thread enviroment we use it in a multithread enviroment
Using our own implemetation --> Can create our own my stack class or Link List
'''
from collections import deque

#Method 1
def Method1():
    stack=[]
    stack.append(10)
    stack.append(20)
    stack.append(30)
    print(stack.pop())
    top=stack[-1]
    print(top)
    size=len(stack)
    print("Size= ",size)
    print("Top element= ",top)
    #O(1)

def Method2():
    stack=deque()
    stack.append(10)
    stack.append(20)
    stack.append(30)
    print(stack.pop())
    top=stack[-1] #In deque also we can use the indexing
    print(top)
    size=len(stack)
    print("Size= ",size)
    print("Top element= ",top)
    #O(1)

#But list has its own advantages
# List is an array implemetation which is more simple and a cache friendly implementation. 
Method1()
print()
print()
Method2()



