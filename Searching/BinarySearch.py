def BinarySearch(l,x):
    low=0
    high=len(l)-1
    while low<=high:
        mid=(high+low)//2
        if l[mid]==x:
            return mid
        elif x<l[mid]:
            high=mid-1
        else:
            low=mid+1
    return -1

l=[10,20,30,40]
e=BinarySearch(l,30)
print(e)