#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:quincyqiang 
@license: Apache Licence 
@file: 英语流利说-二叉排序树.py
@time: 2019-07-30 22:09
@description:
"""
# encoding: utf-8
class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


class BST:
    def __init__(self, node_list):
        self.root = Node(node_list[0])
        for data in node_list[1:]:
            self.insert(data)

    # 搜索
    def search(self, node, parent, data):
        if node is None:
            return False, node, parent
        if node.data == data:
            return True, node, parent
        if node.data > data:
            return self.search(node.lchild, node, data)
        else:
            return self.search(node.rchild, node, data)

    # 插入
    def insert(self, data):
        flag, n, p = self.search(self.root, self.root, data)
        if not flag:
            new_node = Node(data)
            if data > p.data:
                p.rchild = new_node
            else:
                p.lchild = new_node

    def levelTraversel(self, root):
        """
        层次遍历
        """
        res = []
        if root is None:
            return
        queue = []
        queue.append(root)

        while queue:
            node = queue.pop(0)
            res.append(node.data)
            if node.lchild != None:
                queue.append(node.lchild)
            if node.rchild != None:
                queue.append(node.rchild)
        return res


import sys
n = int(sys.stdin.readline().strip())
line = sys.stdin.readline().strip()
values = list(map(int, line.split()))
bst = BST(values)  # 创建二叉查找树
res = bst.levelTraversel(bst.root)
print(" ".join([str(num) for num in res]))
