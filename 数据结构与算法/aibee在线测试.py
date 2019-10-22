#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:quincyqiang 
@license: Apache Licence 
@file: aibee在线测试.py 
@time: 2019-08-18 18:00
@description:
"""
# https://leetcode.com/problems/k-closest-points-to-origin/solution/
# import sys
# line = sys.stdin.readline().strip()
# # P = [num for num in map(int, line.split())]
# P = eval(line)
# K = int(sys.stdin.readline().strip())
# line = sys.stdin.readline().strip()
# Q = eval(line)
#
#
# def kClosest(P, K,Q):
#     P.sort(key=lambda P: (P[0]-Q[0]) ** 2 + (P[1]-Q[1]) ** 2)
#     return P[:K]
#
# print(kClosest(P,K,Q))

# 5,2,1,1,1,1,2
import sys
from collections import Counter
line = sys.stdin.readline().strip()
P = [num for num in map(int, line.split(','))]
print(Counter(P).most_common(1)[0][0])