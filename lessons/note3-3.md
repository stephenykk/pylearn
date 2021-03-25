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