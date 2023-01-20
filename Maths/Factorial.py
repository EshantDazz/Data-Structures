def Fact(n):
    t=n
    while(n>=2):
        t=t*(n-1)
        n-=1
    return t
    
n=int(input("Enter the number  "))
print(Fact(n))