def even_odd(l):
    e=[]
    o=[]
    for x in l:
        if x%2==0:
            e.append(x)
        else:
            o.append(x)
    return e,o

l=[10,45,76,143,87]
e,o=even_odd(l)
print("Even = ",e)
print("Odd = ",o)