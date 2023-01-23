def isPalindome(str,start,end):
    if start>=end:
        return True
    return(str[start]==str[end] and isPalindome(str,start+1,end-1))

s1="Eshant"
s2="malayalam"
print(isPalindome(s1,0,len(s1)-1))
print(isPalindome(s2,0,len(s2)-1))