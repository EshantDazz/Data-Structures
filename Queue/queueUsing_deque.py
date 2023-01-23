from collections import deque
q=deque()
q.append(10)
q.append(20)
q.append(30)
print(q) #To print the queue
print(q.popleft()) #To remove the first element in the queue
q.append(40)
print(q.popleft()) 
print(q)
print("Length of the queue is ",len(q))
print(q[0]) #Front Element
print(q[-1]) #Rear Element


#This is better than List becasue all the implementation is O(1) as deque is a doubly Link List