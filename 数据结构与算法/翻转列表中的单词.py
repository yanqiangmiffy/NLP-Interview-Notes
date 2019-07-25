#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:quincyqiang 
@license: Apache Licence 
@file: 翻转列表中的单词.py
@time: 2019-07-24 13:05
@description:
"""


def reverseWords(s):
    new_string = ""
    j = len(s)
    print(j)
    # iterate the str in a reversed order
    for i in range(len(s) - 1, -1, -1):
        # trim the trailing space
        if s[i] == " ":
            j = i
        # if we encountered a " " before the worlds, we know a word ended here, append " " or the word
        elif i == 0 or s[i - 1] == " ":
            if len(new_string) != 0:
                new_string += " "
            new_string += s[i:j]
        print(i,s[i],new_string)
    return new_string


reverseWords("the sky is blue")

s="the sky is blue"
for i in range(len(s)-1,-1,-1):
    print(i,s[i])
