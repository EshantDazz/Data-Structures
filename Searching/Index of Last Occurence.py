def BinarySearch(l,x):
    high=len(l)-1
    low=0
    while low<=high:
        mid=(low+high)//2
        if x<l[mid]:
            high=mid-1
        elif x>l[mid]:
            low=mid+1
        else:
            if mid==len(l)-1 or l[mid]!=l[mid+1]:
                return mid
            else:
                low=mid+1
    return -1
l=[10,10,11,20,20,20,30,30,40,50]
print(BinarySearch(l,20))