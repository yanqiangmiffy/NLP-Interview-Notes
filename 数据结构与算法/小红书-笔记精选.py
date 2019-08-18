#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:quincyqiang 
@license: Apache Licence 
@file: 小红书-笔记精选.py 
@time: 2019-08-18 15:29
@description:
"""
# 时间限制：C/C++语言 1000MS；其他语言 3000MS
# 内存限制：C/C++语言 65536KB；其他语言 589824KB
# 题目描述：
# 薯队长写了n篇笔记， 编号从 1～n，每篇笔记都获得了不少点赞数。 薯队长想从中选出一些笔记，作一个精选集合。挑选的时候有两个规则：
#
# 1.    不能出现连续编号的笔记。
#
# 2.    总点赞总数最多
#
# 如果满足 1，2条件有多种方案，挑选笔记总数最少的那种。
import sys

n = int(sys.stdin.readline().strip())
index = [i for i in range(n)]
line = sys.stdin.readline().strip()
values = [num for num in map(int, line.split())]

sum=0
n = len(values)
dp = [0] * (n + 1)
if n !=0:
    dp[1] = values[0]
    for i in range(2, n + 1):
        if dp[i - 1]> dp[i - 2] + values[i - 1]:

            dp[i] = dp[i - 1]
        else:
            sum+=1
            dp[i]= dp[i - 2] + values[i - 1]
print(dp[-1],sum)