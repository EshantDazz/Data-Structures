def sumOfDigits(n):
    if n<10:
        return n
    return sumOfDigits(n//10)+n%10

print(sumOfDigits(345)) 