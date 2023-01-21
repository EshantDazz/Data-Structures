#Euclidean Algorithm

def gcd(a,b):
    while(a!=b):
        if a>b:
            a-=b
        else:
            b-=a
    return a
def optimized_gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)


a=12
b=15
print(gcd(a,b))
print(optimized_gcd(a,b))

