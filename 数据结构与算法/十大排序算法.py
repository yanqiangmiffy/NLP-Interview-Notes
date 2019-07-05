#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:quincyqiang 
@license: Apache Licence 
@file: 十大排序算法.py 
@time: 2019-07-05 23:11
@description: https://www.jianshu.com/p/bbbab7fa77a2
"""

nums = [3, 5, 15, 36, 26, 37, 4, 19, 50]


def bubbleSort(nums):
    """
    冒泡排序
    :param nums:
    :return:
    """
    for i in range(len(nums)):
        for j in range(1, len(nums) - i):
            if nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]

    return nums


print("冒泡排序：", bubbleSort(nums))


def selectionSort(nums):
    """
    选择排序
    :param nums:
    :return:
    """
    for i in range(len(nums)):
        minIndex = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[minIndex]:
                minIndex = j
        nums[i], nums[minIndex] = nums[minIndex], nums[i]
    return nums


print("选择排序：", selectionSort(nums))


def insertSort(nums):
    """
    插入排序
    :param nums:
    :return:
    """
    for i in range(1, len(nums)):
        curNum, preIndex = nums[i], i
        while preIndex >= 0 and curNum < nums[preIndex - 1]:
            nums[preIndex] = nums[preIndex - 1]
            preIndex -= 1
        nums[preIndex] = curNum
    return nums


print("插入排序：", insertSort(nums))


def quickSort(nums):
    """
    快速排序
    :param nums:
    :return:
    """
    if len(nums) <= 1:
        return nums
    pivot = nums[0]  # 基准值
    left = [nums[i] for i in range(1, len(nums)) if nums[i] < pivot]
    right = [nums[i] for i in range(1, len(nums)) if nums[i] >= pivot]
    return quickSort(left) + [pivot] + quickSort(right)


print("快速排序：", quickSort(nums))
