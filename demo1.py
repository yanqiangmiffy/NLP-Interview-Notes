#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:quincyqiang 
@license: Apache Licence 
@file: demo1.py 
@time: 2019-07-25 09:42
@description:
"""

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


import numpy as np

X = np.array([1,2,3,4,5,6])
y = np.array([1,2,3,4,5,6])
from sklearn.utils import shuffle
X, y = shuffle(X, y, random_state=0)
print(X,y)