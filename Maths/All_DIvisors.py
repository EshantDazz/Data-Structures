def printDivsors(n):
    i=1
    while(i*i<=n):
        if(n%i==0):
            print(i,end=' ')
            if(i!=n/i):
                print(n//i,end=' ')
        i+=1

def printDivisors2(n):
    i=1
    while(i*i<=n):
        if(n%i==0):
            print(i)
        i+=1
    while(i>=1):
        if n%i==0:
            print(n//i)
        i-=1

n=int(input("Enter a number   "))
print(printDivsors(n))
print(printDivisors2(n))