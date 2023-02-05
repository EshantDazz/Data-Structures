def isSet1(n,k):
    x=1
    for i in range(0,k-1):
        x*=2
    if(x&n!=0):
        return True
    else:
        return False

def EfficientWay(n,k):
    x=1<<(k-1)
    if(x&n!=0):
        return True
    else:
        return False

n=5
k=3
print(isSet1(n,k))
print(EfficientWay(n,k))
