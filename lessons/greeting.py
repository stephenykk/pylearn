# coding: utf-8

sex = input('请输入你的性别（男/女)：')
age = input('请输入你的年龄（1-120）：')

if sex == '男':

    if age >= 18:
       print('你好，帅哥！')
    else:
       print('Hello,小朋友')
else:
    if age > 18:
        print('Hello,美女')
    else:
        print('你好，小姑娘')