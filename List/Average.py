def average(a):
    s=0
    for x in a:
        s+=x
    n=len(a)
    return s/n

l=[10,20,30,40,50]
print(average(l))