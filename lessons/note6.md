# 分支结构

> 知识结构导图 参考 P104

分支结构又称为选择结构，是程序的3中基本结构之一

> 程序有哪三种基本结构？  
> - 顺序
> - 选择(或者说 分支)
> - 循环

生活中，我们有很多根据不同情况做不同决定的情景，比如:
- 如果今天下雨，则带伞
- 如果8点前完成作业，则可以看电视; 否则，继续做作业

## 单分支结构

语法: 

```python
# 如果条件为真(即条件成立)，则执行语句块
# 如果条件为假(即条件不成立)，则执行后面的语句1,语句2
  if <条件>:
     <语句块>
  <语句1>
  <语句2>
```

例子

```python
# 判断用户输入的是不是偶数
a = input('please input a number:')
if a % 2 == 0:
    print('验证成功: 输入的是偶数')
print('执行完毕')
```

例子2

```python
# 判断用户输入的2个数字都是偶数
a = input('a = ')
b = input ('b = ')
if a %2 == 0 and b % 2 == 0:
  print('验证成功: 输入的都是偶数')
print('执行完毕')
```

## 二分支结构

语法:

```python
'''
若条件为真，则执行语句块a; 否则，执行语句块b
'''
if <条件>:
    <语句块a>
else:
    <语句块b>
<语句1>
<语句2>
```

例子

```python
'''
验证用户输入的用户名和密码是否正确
假设正确的用户名为: admin ， 密码为: yang
'''
name = input('name = ')
password = input('password = ')

if name == 'admin' and password == 'yang':
    print('登录成功!')
else:
    print('登录失败!')
```

## 多分支结构

语法

```python
# 多个条件判断
if <条件1>:
    <语句块a>
elif <条件2>:
    <语句块b>
elif <条件3>:
    <语句块c>
else:
    <语句块d>
<语句1>
<语句2>
`
```

例子

```python
# coding: utf-8
score = input('请输入语文成绩:')
if score > 90:
    print('你真优秀')
elif score > 80:
    print('成绩不错呀')
elif score > 70:
    print('要多努力了')
else:
    print('so bad and so sad')
print('执行完毕')
```

例子2

```python
# coding: utf-8
x = input('请输入数值x:')
if x > 1:
    print(3 * x - 5 )
elif x <=1 and x > -1:
    print(x + 10)
else:
    print(x * 10)

print('the end')
```

## 分支结构嵌套

语法

```python
if <条件1>:
    <语句1>
    <语句2>
    if <条件a>:
        <语句块a1>
    else:
        <语句块a2>
else:
    if <条件b>:
        <语句块b>
    <语句3>
    <语句4>
<语句5>
<语句6>
```

例子

```python
age = int(input('请输入你的年龄:'))
grade = int(input('请输入你的年级:'))

if age >= 8:
    if grade >= 3:
        print('恭喜你，你可以玩这个游戏!')
    else:
        print('很遗憾，三年级以下不能玩这个游戏！')
else:
    print('很遗憾，8岁以下不能玩这个游戏!')
print('the end')
```

例子2

```python
# coding: utf-8
# 成绩评级
score = input('请输入你的成绩:')
if score < 60:
    print('不合格呢，要加油啊！')
else:
    if score >= 90:
        print('优秀')
    elif score >= 80:
        print('良好')
    else:
        print('合格')
print('执行完毕')
```

## 练习
抄写下面猜年龄的程序
```python
# coding: utf-8

print('猜猜我几岁?')
age = input('你猜测的年龄是? ')

if age > 10:
    print('你猜大了')
elif age == 10:
    print('真聪明, 你猜对了!')
else:
    print('你猜小了')
print('执行完毕')
```

更多练习参考P115

