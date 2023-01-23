def fact(n):
    if n==1:
        return n
    return n*fact(n-1)

n=int(input("Enter the number "))
if n==0:
    print(1)
elif n<0:
    print('Invalid Input')
else:
    print(fact(n))