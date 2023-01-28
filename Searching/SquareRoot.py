def SquareRoot(x):
    low=1
    high=x
    ans=-1
    while(low<=high):
        mid=(low+high)//2
        sq=mid*mid
        if sq==x:
            return mid 
        elif x<sq:
            high=mid-1
        else:
            low=mid+1
            ans=mid
    return ans

print(SquareRoot(10))
print(SquareRoot(25))