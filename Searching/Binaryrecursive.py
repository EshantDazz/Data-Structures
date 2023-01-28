def Binaryrecursive(l,x,low,high):
    if low>high:
        return -1
    mid=(low+high)//2
    if x==l[mid]:
        return mid
    elif x<l[mid]:
        return Binaryrecursive(l,x,low,mid-1)
    else:
        return Binaryrecursive(l,x,mid+1,high)

def BinarySearch(l,x):
    h=len(l)-1
    n=Binaryrecursive(l,x,0,h)
    return n

l=[10,20,30,40,50,60,70]
print(BinarySearch(l,50))
