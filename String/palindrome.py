def check_Palindrome_1(s):
    low=0
    high=len(s)-1
    while(low<high):
        if(s[low]!=s[high]):
            print("No")
            break
        low+=1
        high-=1
    else:
        print("Yes Palindrome")
def Palindrome_2(s):
    print()
    print("Function 2")
    s2=s[::-1]
    if(s==s2):
        print("yes")
    else:
        print("no")

a=input("Enter the string for which you want to check")
check_Palindrome_1(a)
Palindrome_2(a)