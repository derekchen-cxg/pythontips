#!/usr/bin/env python
L=[]
for i in range(6):
    L.append(input("Enter your number:"))
L.sort()
i=len(L)
if i%2 == 0:
    print(i)
    print(L)
    print(L[int(i/2)],L[int(i/2-1)])
else:
    print(L)
    print(L[int((i-1)/2)])

