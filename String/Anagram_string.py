#If we sort the strings then they become anagram of each other
#We can verify by comparing them

def check_Anagram(s1,s2):
    if(len(s1)!=(len(s2))):
        return False
    count=[0]*256
    for i in range(len(s1)):
        count[ord(s1[i])]+=1
        count[ord(s2[i])]-=1
    for x in count:
        if x!=0:
            return False
    return True

a=input("Enter the first string")
b=input("Enter the second string")
print(check_Anagram(a,b))