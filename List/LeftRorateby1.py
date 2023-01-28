def leftRotate(l):
    s=l[0]
    n=len(l)
    for i in range(1,n):
        l[i-1]=l[i]
    l[n-1]=l[0]
l=[23,54,66,199]
leftRotate(l)
print(l)
