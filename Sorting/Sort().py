l1=[23,54,1,100,35,99]
l2=[23,54,1,100,35,99]

l1.sort()
l2.sort(reverse=True)
print(l1)
print(l2)


#Sorting Using key

def Sort_Based_on_Lnegth(l):
    return len(l)

l3=['Eshant','Das','Data_Science']
l3.sort(key=Sort_Based_on_Lnegth,reverse=True)
print(l3)



#Sorting User defined Objects
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __lt__(self,other):
        if self.x==other.x:
            return self.y<other.y
        else:
            return self.x<other.x
l=[Point(2,30),Point(2,10),Point(10,4),Point(6,7)]
l.sort()
# print(l) this won't print the actaul list
for i in l:
    print(i.x,i.y,end=', ')

'''
1. Uses Tim Sort
2. Stable
3. Works only for List
4. Modifies the same List
'''