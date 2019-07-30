#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:quincyqiang 
@license: Apache Licence 
@file: demo1.py 
@time: 2019-07-25 09:42
@description:
"""

# a = input().split()
# n, m = int(a[0]), int(a[1])
#
# K=0
# for i in range(n):
#     for j in range(i + 1, n):
#         K+=1
# arr = []
# up = [0 for i in range(n+1)]
# down = [0 for i in range(n+1)]
# for i in range(K):
#     arr.append([int(num) for num in input().split()])
#
# for i in range(K):
#     up[arr[i][0]] = up[arr[i][0]] + arr[i][2]
#     down[arr[i][1]] = down[arr[i][1]] + arr[i][2]
#
# for i in range(1,n+1):
#     up[i] = up[i] + up[i-1]
#     down[i] = down[i] + down[i-1]
#
# ans = []
# for i in range(1,n):
#     ans.append(m -up[i]+down[i])
# print(K)
# print(" ".join([str(i) for i in ans]))


# 1
# import sys
# if __name__ == '__main__':
#
#     # a = [1, 3, 7, 4, 10]
#     # b = [2, 1, 5, 8, 9]
#     line = sys.stdin.readline().strip()
#     # 把每一行的数字分隔后转化成int列表
#     a = list(map(int, line.split()))
#
#     line = sys.stdin.readline().strip()
#     # 把每一行的数字分隔后转化成int列表
#     b = list(map(int, line.split()))
#
#     def find_b(s, e):
#         b.sort(reverse=True)
#         for num in b:
#             if num < e and num > s:
#                 return num
#
#     flag=False
#     for i in range(1, len(a)):
#         if a[i] < a[i - 1]:
#             if find_b(a[i-1],a[i+1]):
#                 a[i]=find_b(a[i-1],a[i+1])
#                 flag=True
#                 break
#     if flag:
#         print(" ".join([str(num) for num in a ]))
#     else:
#         print("NO")

# 2
# import sys
# if __name__ == '__main__':
#
#     line=sys.stdin.readline().strip()
#     # CAT TIGER RPC
#     flag=True
#     new_line=line.replace(' ','')
#     if len(new_line)==len(set(new_line)):
#         flag=False
#     else:
#         words=line.split()
#         if not set.intersection(set(words[0]),set(words[-1])):
#             flag = False
#         else:
#             for i in range(1,len(words)):
#                 if not set.intersection(set(words[i]),set(words[i-1])):
#                     flag = False
#                     break
#     if flag:
#         print("true")
#     else:
#         print("false")


# 4

import sys

if __name__ == '__main__':

    line = sys.stdin.readline().strip()
    N = int(line)

    line = sys.stdin.readline().strip()
    Li = list(map(int, line.split()))

    line = sys.stdin.readline().strip()
    Wi = list(map(int, line.split()))

    lw = dict(zip(Wi, Li))
    Li.sort(reverse=True)
    Wi.sort(key=lambda x: lw[x], reverse=True)
    height = 1
    for i, wi in enumerate(Wi):
        print(i)
        cur_sum = 0
        cur_height = 0
        for j in Wi[i + 1:]:
            if cur_sum <= sum(7 * [Wi[i]]):
                cur_sum += Wi[j]
                cur_height += 1
        height = max(cur_height, height)
    print(height)

from simhash import Simhash
from nltk import ngrams


def extract_hash_feature(df):
    def get_ngrams(sequence, n=2):
        return ['_'.join(ngram) for ngram in ngrams(sequence, n)]

    def calculate_simhash_dist(sequence1, sequence2):
        return Simhash(sequence1).distance(Simhash(sequence2))

    def calculate_all_simhash(row):
        query, title = row['query'].split(), row['title'].split()
        simhash_w1gram_dist = calculate_simhash_dist(query, title)
        simhash_w2gram_dist = calculate_simhash_dist(get_ngrams(query, 2), get_ngrams(title, 2))
        simhash_w3gram_dist = calculate_simhash_dist(get_ngrams(query, 3), get_ngrams(title, 3))
        return '{}:{}:{}'.format(simhash_w1gram_dist, simhash_w2gram_dist, simhash_w3gram_dist)

    df['sim_hash'] = df.apply(calculate_all_simhash, axis=1, raw=True)
    df['simhash_w1gram_dist'] = df['sim_hash'].apply(lambda x: float(x.split(':')[0]))
    df['simhash_w2gram_dist'] = df['sim_hash'].apply(lambda x: float(x.split(':')[1]))
    df['simhash_w3gram_dist'] = df['sim_hash'].apply(lambda x: float(x.split(':')[2]))
    del df['sim_hash']
