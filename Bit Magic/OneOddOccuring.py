def Naive(arr):
    n=len(arr)
    for i in range(0,n):
        c=0
        for j in range(0,n):
            if(arr[j]==arr[i]):
                c+=1
        if c%2!=0:
            return arr[i]

    return None

def Efficent(arr):
    n=len(arr)
    res=arr[0]
    for i in range(1,n):
        res=res^arr[i]
    return res

l=[2,3,4,4,3,4,4,2,3]
print(Naive(l))
print(Efficent(l))

