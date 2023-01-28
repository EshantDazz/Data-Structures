def isSorted(l):
    for i in range(1,len(l)):
        if l[i]<l[i-1]:
            return False
    return True

a=[10,20,35,78]
print(isSorted(a))