#In subsequence the order should be same 

def subsequence(s1,s2):
    i,j=0,0
    while(i<len(s1) and j<len(s2)):
        if(s1[i] == s2[j]):
            j+=1
        i+=1
    if j==len(s2):
        return True
    else:
        return False



a=input("Enter the first string ")
b=input("Enter the second string to check if subsequent")
print(subsequence(a,b))


