def reversee(l):
    s=0
    e=len(l)-1
    while(s<e):
        l[s],l[e]=l[e],l[s]
        s+=1
        e-=1

l=[10,20,30]
reversee(l)
print(l)
