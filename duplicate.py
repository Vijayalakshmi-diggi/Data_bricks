a=[1,2,3,4,5,4,5,2]
b=[]
c=[]
for ch in a:
    if ch not in b:
        b.append(ch)
    else:
        c.append(ch)
print(b)
print(c)