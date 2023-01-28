def removeDuplicates(l):
    r=1
    for i in range(1,len(l)):
        if l[r-1]!=l[i]:
            l[r]=l[i]
            r+=1
    return r

l=[10,10,20,20,20,30,40,50,60,60]
n=removeDuplicates(l)
for i in range(n):
    print(l[i],end=' ')