def Naive(n):
    c=0
    while(n>0):
        if(n&1!=0):
            c+=1
        n//=2
    return c

def BrianKerningramsAlgorithm(n):
    c=0
    while(n!=0):
        c+=1
        n=n&(n-1)
    return c
print(Naive(5))
print(BrianKerningramsAlgorithm(5))