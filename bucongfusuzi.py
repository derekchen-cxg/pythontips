#!/usr/bin/env
s="45678"
a=[]
c=[]
b=""
for x in range(len(s)):
    for y in range(len(s)):
        for z in range(len(s)):
            b=str(s[z])+str(s[y])+str(s[x])
            if b[0] != b[1] and b[0] != b[2] and b[1] != b[2]:
                a.append(b)
            else:
                c.append(b)
print(a)
print(c)


