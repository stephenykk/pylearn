# 字符串

## 字符串的运算

### 字符串加法
用加号`+`可以把多个字符串，连接起来

```python
s = 'hello' + "world"
print(s) # helloworld
```

### 字符串乘法
用乘号`*`可以把字符串重复n遍。

```python
s = 'hi' * 3
print(s) # hihihi
```

### 字符串索引
**索引就是下标** ， 通过索引可以获取字符串的指定位置的那个字符

索引分**正向索引**和**反向索引**

**注意：索引号是从0开始的**

<table>
<tr>
<th>字符串</th><td colspan="4" align="center">blue</td>
</tr>
<tr>
<th>正向索引</th><td>0</td><td>1</td><td>2</td><td>3</td>
</tr>
<tr>
<th>反向索引</th><td>-4</td><td>-3</td><td>-2</td><td>-1</td>
</tr>
<tr>
<th>对应字符</th><td>b</td><td>l</td><td>u</td><td>e</td>
</tr>
</table>

例子

```python
s = 'blue'

# 索引号用中括号包着 [n]
print(s[0]) # b
print(s[1]) # l

print(s[-4]) # b
print(s[-1]) # e
```