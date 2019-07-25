#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:quincyqiang 
@license: Apache Licence 
@file: demo1.py 
@time: 2019-07-25 09:42
@description:
"""

a = input().split()
n, m = int(a[0]), int(a[1])

K=0
for i in range(n):
    for j in range(i + 1, n):
        K+=1
arr = []
up = [0 for i in range(n+1)]
down = [0 for i in range(n+1)]
for i in range(K):
    arr.append([int(num) for num in input().split()])

for i in range(K):
    up[arr[i][0]] = up[arr[i][0]] + arr[i][2]
    down[arr[i][1]] = down[arr[i][1]] + arr[i][2]

for i in range(1,n+1):
    up[i] = up[i] + up[i-1]
    down[i] = down[i] + down[i-1]

ans = []
for i in range(1,n):
    ans.append(m -up[i]+down[i])
print(K)
print(" ".join([str(i) for i in ans]))

