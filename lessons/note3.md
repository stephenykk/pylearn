# 字符串类型

字符串由字母、数字、下划线和中文等组成，是最常用的数据类型。

字符串举例
```python
s = 'hello'
s = '100'
s = 'hello 100 last_one long-short'
s = '你好python,今天是周末'
```

## 字符串的表示方式

1. 单引号或双引号字符串
    ```python
    # 单引号或双引号包裹表示字符串
    s = 'hello world'
    s = "hello world"
    ```
2. 三引号字符串
    ```python
    # 三个单引号或三个双引号包裹，表示字符串
    # 三引号字符串，可以输出换行的内容
    s = '''床前明月光
    疑是地上霜'''
    print(s)
    s = """床前明月光
    疑是地上霜"""
    ```

## 转义字符
转义字符是什么？  
就如字面意思：**转换了意义的字符**

转义字符举例
```python
# \n \t 就是转义字符
str = 'hello \n world'
str = 'ni \t hao'
```

**转义字符**相对的就是**普通字符**

**普通字符的含义**是很好理解的，如下表：

<table>
<tr>
    <th>字符</th><th>\</th><th>t</th><th>n</th><th>a</th><th>b</th>
</tr>
<tr>
    <td>含意</td><td>反斜线</td><td>字母t</td><td>字母n</td><td>字母a</td><td>字母b</td>
</tr>
</table>

为什么需要转义字符呢？  
因为有一些不可见字符，无法用来字母表示，比如：回车符 tab符; 所以需要对字符转换意义，让它们能表示这些不可见字符。

字符默认含意和新含意对照表

**注意：`\`是非常特殊的，它的默认含意是把后面的字符转义**

<table>
<tr>
    <th>字符</th><th>默认含意</th><th>转义写法</th><th>转义后的含意</th>
</tr>
<tr>
    <td>\</td><td>把后面的字符转义</td><td>\\</td><td>反斜线</td>
</tr>
<tr>
    <td>n</td><td>字母n</td><td>\n</td><td>换行符</td>
</tr>
<tr>
    <td>t</td><td>字母t</td><td>\t</td><td>tab符</td>
</tr>
<tr>
    <td>b</td><td>字母b</td><td>\b</td><td>删除键</td>
</tr>
<tr>
    <td>'</td><td>字符串开始或结束标记</td><td>\'</td><td>单引号</td>
</tr>
<tr>
    <td>"</td><td>字符串开始或结束标记</td><td>\"</td><td>双引号</td>
</tr>
</table>

例子
```python
# 用转义符 \n 表示换行
print('hello\nworld')
print('xiaohua\'s book')
print('换行的转义符是:\\n')

s = 'python中使用"\\"对字符进行转义，例如：换行使用转义符"\\n"表示'
print(s)
```

