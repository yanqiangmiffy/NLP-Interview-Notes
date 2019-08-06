#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:quincyqiang 
@license: Apache Licence 
@file: 02.贪心_最优装载问题.py 
@time: 2019-08-06 23:00
@description:
船容量为C，古董重量为Wi
"""
from typing import List


def most_nums(C: int, W: List[int]) -> int:
    W.sort()
    tmp=0
    ans=0
    for w in W:
        tmp+=w
        if tmp<=C:
            ans+=1
    return ans

if __name__ == '__main__':
    C=30
    W=[4,10,7,11,3,5,14,2]
    print(most_nums(C,W))