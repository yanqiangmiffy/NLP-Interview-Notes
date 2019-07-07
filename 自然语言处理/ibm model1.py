#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:quincyqiang 
@license: Apache Licence 
@file: ibm model1.py 
@time: 2019-07-07 15:39
@description:
"""
import operator
from functools import reduce
CORPUS_CH = [['一本', '书'], ['一本', '杂志'], ['这本', '书'], ['这本', '杂志'], ]
CORPUS_EN = [['a', 'book'], ['a', 'magazine'], ['this', 'book'], ['this', 'magazine'], ]
f_word = list(set(reduce(operator.add, CORPUS_CH)))
e_word = list(set(reduce(operator.add, CORPUS_EN)))
T = {}

for k in range(5):
    C = {}
    for m, l in zip(CORPUS_CH, CORPUS_EN):
        if k == 0:
            for fi in m:
                for ej in l:
                    if " % s| % s" % (fi, ej) not in T:
                        T[" %s| % s" % (fi, ej)] = 1.0 / len(e_word)
        for i, fi in enumerate(m):
            sum_t = sum([T[" % s| % s" % (fi, ej)] for ej in l]) * 1.0
            for j, ej in enumerate(l):
                delta = T[" % s| % s" % (fi, ej)] / sum_t
                C[" % s % s" % (ej, fi)] = C.get(" % s % s" % (ej, fi), 0) + delta
                C[" % s" % (ej)] = C.get(" % s" % (ej), 0) + delta
    print("---iteration: % s---" % (k))
    for key in T:
        print(key, ":", T[key])
    for f in f_word:
        for e in e_word:
            if " % s % s" % (e, f) in C and " % s" % (e) in C:
                T[" % s| % s" % (f, e)] = C[" % s % s" % (e, f)] / C[" % s" % (e)]

print("---iteration: % s---" % (k + 1))
for key in T:
    print(    key, ":", T[key])

