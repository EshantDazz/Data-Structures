def Naive(n):
    if n==0:
        return False
    while(n!=1):
        if(n%2!=0):
            return False
        n//=2
    return True

def BrianKerningramsAlgorithm(n):
    if n==0:
        return False
    return (n&(n-1)==0)