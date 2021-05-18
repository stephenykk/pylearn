# 条件循环

## while循环语句

预先不知道要执行多少次，反正条件成立就一直执行，直到条件不成立

> 如果条件一直都成立，那么就是死循环了，所以循环要注意让其能够结束

while循环语法

```python
while <条件>:
    # 通常语句块里头要做一些事情 让条件不能成立
    <语句块>
```

例子
```python

# 计算1+...+100的和
s = 0
i = 1
while i <= 100:
    s += i
print(s)
```

无限循环例子
```python
while True:
    num = input('input a number:')
    print('your number is: %d' % num)

# 下面的语句永远不会执行到
print('goodbye')

> 0 空字符串('') 空列表([]) False 都认为是假值

例子
```python
# coding: utf-8
word = input('请输入单词:')
while word:
    print(word.upper())
    word = input('请继续输入单词:')
print('执行完毕')
```

### break语句和continue语句

for循环和while循环中，用**break**退出循环，用**continue**立即进入下次循环

例子

```python
# coding: utf-8
# 当遍历到lufy时，退出循环
roles = ['nami', 'robin', 'lufy', 'zoro']
for role in roles:
    if role == 'lufy':
        break;
    print('当前角色是:' + role)
print('the end')
```

例子2

```python
# coding: utf-8
# 当遍历到lufy时，立即进入下次循环，不往下执行循环体内剩余的语句
roles = ['nami', 'robin', 'lufy', 'zoro']
for role in roles:
    if role == 'lufy':
        break;
    print('当前角色是:' + role)
print('the end')
```

## 循环结构的嵌套

for循环的循环体内又有for循环，这样的结构称之为循环嵌套

例子

```python
# 打印乘法表
for i in range(10):
    for j in range(10):
        print('%d * %d = %d' % (i, j, i * j))
print('the end')
```


## 循环结构和分支结构的组合

例子

```python
# 输出0-100中7的倍数的个数
n = 0
ls = []
for i in range(101):
    if i % 7 == 0:
        n += 1
        ls.push(i)
print(n, ls)
```

例子2
```python
# 把正数和负数分开，放在2个列笔中
numbers = [1, 4, -2, 3, -8, 9, -33]
alist = []
blist = []
for num in numbers:
    if num >= 0:
        alist.append(num)
    else:
        blist.append(num)

print(alist)
print(blist)
```

## 练习
1. 编写程序，求出1～100中所有偶数的和

2. 编写程序，输出数字 5,6,7,...100

3. 更多习题 参考P132
