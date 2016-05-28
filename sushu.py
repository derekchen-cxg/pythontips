#!/usr/bin/python
for x in range(1,101):
    for y in range(1,101):
        if x<=y:
           # print(x)
            break
        elif x%x==0 and x%y==0:
            print(x)
#            print(' '.join(str(x)))