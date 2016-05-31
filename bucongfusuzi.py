#!/usr/bin/env
a=[]
c=[]
b=""
for x in range(1,5):
    for y in range(1,5):
        for z in range(1,5):
            b=str(z)+str(y)+str(x)
            if b[0] != b[1] and b[0] != b[2] and b[1] != b[2]:
                a.append(b)
            else:
                c.append(b)
print(a)
print(c)


