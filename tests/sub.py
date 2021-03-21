#!/usr/bin/python3
# coding:utf-8
a = input('请输入数字1: ')
b = input('请输入数字2: ')
lst = [int(a),int(b)]

big = max(lst)
small = min(lst)

result = big - small

print('两个数的差为:', result)


