from urllib.request import AbstractDigestAuthHandler


def check_rotation(s1,s2):
    t=''
    t=s1+s1
    return len(s1)==len(s2) and s2 in t

a=input("Enter the string")
b=input("Enter the second string")
print(check_rotation(a,b))