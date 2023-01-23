def getSmaller(l,n):
    a=[]
    for x in l:
        if x<n:
            a.append(x)
    return a

l=[14,56,87,12,768,12,564]
n=90
print(getSmaller(l,n))