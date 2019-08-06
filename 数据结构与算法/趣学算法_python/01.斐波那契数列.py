#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:quincyqiang 
@license: Apache Licence 
@file: 01.斐波那契数列.py 
@time: 2019-08-06 22:51
@description:

1 1 2 3 5 8 13 21 34
"""


def fib1(n: int) -> int:
    """
    斐波那契数列 递归
    :param n:
    :return:
    """
    if n == 1 or n == 2:
        return 1
    else:
        return fib1(n - 1) + fib1(n - 2)


def fib2(n: int) -> int:
    dp = [0 for i in range(n)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n):
        dp = dp[i - 2] + dp[i - 1]
    return dp[n - 1]


if __name__ == '__main__':
    print(fib1(3))
