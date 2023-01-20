def isPal(n):
    rev=0
    temp=n
    while(n!=0):
        d=n%10
        rev=rev*10+d
        n//=10
    return rev==temp

n=int(input("Enter the number  "))
print(isPal(n))