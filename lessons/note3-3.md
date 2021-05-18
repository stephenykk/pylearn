# python的基础语法

## 字符串的常用方法

### count()方法
用于统计子字符串在指定范围内出现的次数

语法: `str.count(sub, start, end)`

- sub 要查找的子字符串
- start 开始索引
- end 结束索引

例子

```python
s = 'have a good day'
sub = 'a'
# print(s.count('a')) # 同下
print(s.count(sub)) # 3

print(s.count(sub, 0, 4)) # 1
```

### find()方法
用于查找子字符串出现的位置，如果没找到，则返回-1

语法: `str.find(sub, start, end)`

- str 字符串
- sub 要查找的子字符串
- start 开始索引 默认为0
- end 结束索引 默认为字符串末尾

例子

```python
s = 'Hello Sunday!'
sub = 'Sun'
print(s.find(sub)) # 6

```

### join()方法
用当前字符串将一组字符串连接起来。

语法 `str.join(iterable)`

- str 连接用的字符串
- iterable  可遍历的对象(*包括：字符串、列表等*)

例子

```python
'''
可遍历对象: 就是可以用for去访问每个成员的对象
例如: 字符串就是可遍历对象
'''
for c in 'monday':
  print(c)

s = 'hello'
a = '-'
print(a.join(s)) # h-e-l-l-o
```

### split()方法
把字符串以指定字符为分隔标记，拆分为列表。

语法 `str.split(sep, maxsplit=-1)`

- str 将要被拆分的字符串 默认为全部空白字符(*空格 tab 换行*)
- sep 作为分隔标记的字符
- maxsplit 最多拆分多少下 默认为-1 即有多少拆分多少

例子

```python
s = 'go for job'
s.split(' ') # ['go', 'for', 'job']
s.split(' ', 1) # ['go', 'for job']
s.split('o') # ['g', ' f', 'r j', 'b']

# 分隔符默认为 空格
s.split() # ['go', 'for', 'job']
```

### len()函数
`len()`函数是python内置函数，可用户返回字符串的长度。

语法: `len(str)`

例子

```python
s = 'hello sunday'
print(len(s)) # 打印s有多少个字符
```

### 字符串遍历
python语言中用for实现遍历

> 遍历是什么意思  
> 从第一个查看到最后一个  
> 比如 老师批改全班的试卷，其实，就是老师把一叠卷子，从第一张，改到最后一张，这就是遍历，遍历时做的事情是批改和打分

用for遍历字符串

例子

```python
# 方法1 直接遍历
string = 'hello world!'
for c in string:
  print(c)


# 方法2 用索引遍历
string = 'school'
# range(len(s)) # [0, 1, 2, 3, 4, 5]
for i in range(len(string)):
  print(string[i])
```


