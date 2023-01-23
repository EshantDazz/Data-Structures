def secondLargest(l):
    if len(l)<=1:
        return None
    la=l[0]
    se=None
    for x in range(1,len(l)):
        if l[x]>la:
            se=la
            la=l[x]
        elif l[x]!=la:
            if se<l[x]or se==None:
                se=l[x]
    return se
 
a=[23,45,1,56,87,100]
print(secondLargest(a))

