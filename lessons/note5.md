# 数据类型转换

> 知识结构导图 参考P97

数据类型转换就是把数据从一种类型转换为另一种类型

数据类型转换函数

函数  | 说明 | 例子
--- | --- | ---
int(x) | 转换为整数 | `int('20')` 结果为 20
float(x) | 转换为浮点数 | `float(3)` 结果为 3.0
str(x)  | 转换为字符串 | `str(30)` 结果为 '30'
list(x) | 转换为列表 | `list('hello')` 结果为 ['h', 'e', 'l', 'l', 'o']

例子

```python
print(int(10.33))
print(int('20'))


# 只要字符串内包含非数字字符都会报错
print(int('21.35'))
print(int('世界'))
print(int('good'))

print(float(5))
print(float('23.33'))  # 字符串内包含. 不会报错 因为浮点型

# 只要字符串内包含数字和.之外的字符都会报错
print(float('good'))
print(float('未来'))

number = 10
price = 2.4

strNum = str(number)
strPrice = str(price)

# type函数返回变量的类型
print(type(strNum))
print(type(strPrice))

mylist = list('sunny')
print(mylist)

```


## 练习

1. 参考P101习题

