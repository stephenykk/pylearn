# 列表

## 列表元素的修改

语法: `listName[index] = 新元素`

通过索引修改列表元素

例子

```python
scores = [90, 89, 99]
scores[2] = 100
print(scores)

```

## 列表的统计

列表统计指的是统计什么？
- 特定元素出现的次数
- 列表的长度
- 所有元素的和
- 最大的元素
- ...

相关方法：

方法或函数 | 说明 | 例子
--- | --- | ---
count() | 返回列表中指定元素的个数 | `mylist.count('A')`
index() | 返回列表中指定元素首次出现的位置 | `mylist.index('C')`
len()  | 返回列表的长度(*即: 元素的个数*) | `len(mylist)`
sum() | 返回列表所有元素的和 | `sum(mylist)` 列表元素需要都是数值类型
max() | 返回列表的最大元素 | `max(mylist)` 列表yuansuu需要都是数值类型
min() | 返回列表的最小元素 | `min(mylist)` 列表元素需要都是数值

例子

```python
mylist = ['a', 'b', 'c', 'd', 'b', 'b', 'e']
print(mylist.count('b'))
print(mylist.index('d'))
print(len(mylist))

list2 = [9, 20, 2, 3]
print(sum(list2))
print(max(list2))
print(min(list2))

```

## 列表的排序

语法: `listName.sort(key = None, reverse = False)`

- listName: 要排序的列表
- key: 从每个元素提取用于比较的键
- reverse: 是否降序

```python
scores = [100, 93, 88,78,91]
scores.sort()
print(scores)

scores.sort(reverse = True)
print(scores)

```


## 练习
1. 先思考，并抄写下面程序

```python
str = ''
for i in ['a', 'b', 'c', 'd']:
    str = str + i

print(str) # ?
```

2. 参考P88的习题

