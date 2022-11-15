from codecs import charmap_build


CHAR = 256 
def leftmost(st) :
    count = [0] * CHAR 
    for i in range(len(st)) :
        count[ord(st[i])] += 1 
    for i in range(len(st)) :
        if count[ord(st[i])] > 1 :
            return i 
    return -1 

def leftmost2(s):
    isvisited=[False]*CHAR
    res=-1
    for i in range(len(s)-1,-1,-1):
        if(isvisited[ord(s[i])]==True):
            res=i
        else:
            isvisited[ord(s[i])]=True
    return res 

a=input("Enter the a string")
print(leftmost(a))
print()
print(leftmost2(a))
