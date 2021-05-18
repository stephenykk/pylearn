# 循环结构

> 计算机的计算速度很快，很擅长做重复的事情

for循环语句常用来遍历列表、字符串等可遍历对象

> 遍历是什么意思？  
> 就是每个元素都访问一下

语法

```python
    for <循环变量> in <可遍历对象>:
        # for内部的语句块也叫循环体
        <循环体/语句块>
```

## 计数循环
事先知道要循环多少次

for循环语句常常和`rang()`函数一起使用

### range()

`rang()`用于生成整数序列

语法: `range(start, end, step)`

- start 计数开始值，默认0
- end 计数结束值，但不包含该值
- step 步长 序列中相邻两数的差值

例子
```python
range(2) # [0, 1]
range(3) # [0, 1, 2]
range(2, 5) # [2, 3, 4]
range(2, 8, 2) # [2, 4, 6]
range(8, 2, -2) # [8, 6, 4]
```

计数循环例子/整数列表遍历

```python
# range(5) 生成了一个列表 [0, 1, 2, 3, 4]
# 然后用for遍历这个列表
for i in range(5):
    print(i)

# 计算1+...+100的和
s = 0
for i in range(0, 101):
    s += i
print(s)
```

列表遍历例子

```python
# coding: utf-8
books = ['水浒传','三国演义', '红楼梦', '西游记']
for book in books:
    print(book)

```

例子：找最大元素
```python
# coding: utf-8
alist = [12, 43, 20, 56, 33]

a = alist[0]
for i in range(len(alist)):
    if alist[i] > a:
        a = alist[i]

print('最大的元素是: %d' % a)
```

例子：字符串遍历
```python
for c in 'school':
    print(c)
```
