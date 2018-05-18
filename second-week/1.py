
import os
import numpy as np


a = open("zhuanzhi.txt","r")

#print(a)
b =[]
for line in a.readlines():
    b.append(line.strip().split("\t"))

#print(b)

c = np.array(b)

#print(c)

d = c.T

print(d) #利用numpy的转制函数


print (map(list,zip(*b))) #利用了zip函数


listb=[[r[col] for r in b] for col in range(len(b[0]))]

print(listb) #用了for循环
