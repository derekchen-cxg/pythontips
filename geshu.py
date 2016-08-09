#!/usr/bin/env python
'''
给你一个正整数列表 L, 如 L=[2,8,3,50], 输出L内所有数字的乘积末尾0的个数,
如样例L的结果为2.(提示:不要直接相乘,数字很多,可能溢出)
#a=input('please input the number:')
'''
L = [2,8,3,50,85]
y = 1
n = 0

#正向循环
for x in L:
    y = y*x
print(y)

#反向循环
for z in str(y)[::-1]:
    #注意和 if z == 0:的区别
    if z == "0":
        n = n+1
    else:
        break
print(n)




