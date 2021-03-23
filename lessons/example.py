# coding: utf-8

value1 = input('请输入数字(1 代表下雨 0 代表不下雨): ')
value2 = input('请输入数字(1 代表有作业 0代表没作业): ')

rainy = int(value1) > 0
buzy = int(value2) > 0

if rainy or buzy:
    print('我只能呆在家里:(')

if not rainy and not buzy:
    print('我可以去公园玩:)')

if not buzy:
    print('我有空，可以在家看电视或去公园玩')

