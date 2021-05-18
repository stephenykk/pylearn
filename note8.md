# 异常处理

什么叫**异常**  
程序运行过程中，遇到的各种错误，就叫异常，俗称**bug**

程序发生异常时，我们需要捕获并处理它，不然程序就会终止执行(*没完成预期的事情，就意外退出*)  

## `try...except`语句

python用`try...except`语句捕获异常

语法:

```python
try:
    <可能抛出异常的语句块>
except:
    <捕获到异常要执行的处理语句>
```

例子
```python
# coding: utf-8
# 判断用户输入的数字是几位数
a = input('请输入一个整数:')
a = int(a)
count = 0
while a != 0:
    count += 1
    a = a // 10
print('你输入的是%d位整数' % count)

# 如果用户输入的不是数字，上面的程序会出错(*抛出异常*)
```

下面用`try...except`语句来完善它

```python
# coding: utf-8
# 判断用户输入的数字是几位数
try:
    a = input('请输入一个整数:')
    a = int(a)
    count = 0
    while a != 0:
        count += 1
        a = a // 10
    print('你输入的是%d位整数' % count)
except:
    print('输入有误，请输入整数')
```

## `try...except...else`语句

当没有异常发生时，将执行else语句块

语法:

```python
try:
    <可能会抛出异常的语句块>
except:
    <异常处理语句>
else:
    <没有发生异常执行的语句块>

```

例子

```python
# coding: utf-8
# 如果用户没有按提示输入数值，则会发生异常
try:
    a = input('请输入一个整数:')
    b = input('请输入一个浮点数:')
    c = a + b
except:
    print('输入有误')
else:
    print(c)
```

## `try...except..finally`语句

完整的异常处理语句应该包含finally语句块, 无论程序是否发生异常，finally语句块都会执行

语法:

```python
try:
    <可能抛出异常的语句块>
except:
    <处理异常>
finally:
    <无论是否异常都执行的语句块>

```

例子

```python
try:
    a = int(input('请输入一个整数：'))
    b = input('请输入一个字符串: ')
    c = a * b
except:
    print('输入有误')
finally:
    print('字符串的重复输出')
```

## 练习
1. 习题参考 P143
