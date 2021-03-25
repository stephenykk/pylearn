# python的基础语法

## 字符串运算

### 字符串切片
编程中，经常会有需要截取字符串片段的情况; 这个时候可以用切片语法。

语法: `str[start:end:step]`

- start 开始索引
- end  结束索引
- step 步长，隔多少个取一个出来

例子
```python
s = 'Hello Python!'
print(s[1:5]) # ello
print(s[6:-1]) # Python
print(s[-7:-2]) # pytho

m = 'happy day'

'''
省略start则默认为0, 相当于[0:-1] 
结果为 happy da
'''
print(m[:-1]) 

'''
省略end则默认为最末尾，
结果为 apply day
'''
print(m[1:]) 

'''
start和end都省略，相当于从头取到尾(即取整个字符串)，
这里指定step为2, 表示走2步取一个字符，
所以结果为hpydy
'''
print(m[::2]) 

n = 'one day!'
'''
要截取字符串day
有如下三种方法
'''
# 只有正向索引
print(n[4:7])

# 用正向和反向索引
print(n[4:-1])

# 只用反向索引
print(n[-4:-1])

```

### 成员运算符
成员运算符`in` 或 `not in`, 用于检测字符串是否包含指定的字符或子字符串，包含返回`True`, 不包含则返回`False`。

例子
```python
s = 'blue sky'
print('b' in s)
print('sk' in s)
print('sky' in s)
print('m' not in s)
print('que' not in s)
```

