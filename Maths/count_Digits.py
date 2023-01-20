def count(n):
    c=0
    while(n!=0):
        n//=10
        c+=1
    
    return c

n=int(input("Enter the number"))
print(count(n))

