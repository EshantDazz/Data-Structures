l=[2,343,23,43,100,6,87]
m=l[0]
for x in range(len(l)-1):
    if m<l[x+1]:
        m=l[x+1]
print(m)


