q=[]
q.append(10)
q.append(20)
q.append(30)
print(q) #To print the queue
print(q.pop(0)) #To remove the first element in the queue
q.append(40)
print(q.pop(0)) #O(n)
print(q)
print("Length of the queue is ",len(q))
print(q[0]) #Front Element
print(q[-1]) #Rear Element