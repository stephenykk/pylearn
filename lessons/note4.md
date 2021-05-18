# 列表

> 知识结构导图，参考P70

什么是列表  
列表就是一组值，或者说一队列值。

通过前面的学习，我们知道变量即容器，可以保存各种值（*字符串，整数*)  
但是，一个变量只能保存一个值;  
如果我想用变量保存我多个朋友的名字，就得用多个变量，如:  
```python
a = 'nami'
b = 'lufy'
c = 'robin'
```
这会很麻烦，所以就有**列表**类型，可以让一个变量保存一组值
```python
myFriends = ['nami', 'lufy', 'robin']
```

## 列表创建

语法: `listName=[元素1, 元素2, ...]`  

元素放在`[]`中，元素之间用`,`隔开, 列表中的元素可以是不同的数据类型(*即: 元素1可以是字符串，元素2可以是整数，不要求每个元素数据类型相同*)

例子

```python
list1 = [10, 20, 30]
list2 = ['one', 'two', 'three']
list3 = [20, 'hello', ['李白', '杜甫'], True]
print(list3)
```

## 列表的删除

语法: `del listName`

例子

```python
subjects = ['match', 'english']
print(subjects)
del subjects
print(subjects) # 列表被删除后，已经不存在 打印它会报错
```


## 列表的索引和访问
列表的索引和字符串的索引相同，支持正索引和负索引

```python
places = ['home', 'school', 'street']
print(places[0]) # home
print(places[-1]) # street
print(places[1]) # school

# 字符串分割为列表
string = 'long-way'
string.split('-') # ['long', 'way']
```
## 列表元素的添加

方法 | 说明 | 例子
--- | ---- | ---
append()  | 在列表末尾追加一个元素 | `friends.append('lufy')`
extend()  | 在列表末尾追加一个新列表 | `friends.extend(['lufy', 'robin'])`
insert() | 在列表指定位置插入一个元素 | `friends.insert(1, 'zoro')`

例子

```python
mylist = ['A']
mylist.append('B')
print(mylist)

newlist = ['C', 'D']
mylist.extend(newlist)
print(mylist)

mylist.insert(1, 'E')
print(mylist)

```

## 列表元素的移除

方法  | 说明  | 例子
--- | --- | ---
del listName[index] | 删除指定索引位置的数据 | `del mylist[1]`
remove()  | 移除列表中某个值的第一个匹配项 | `mylist.remove('C')` **无返回值**
pop() | 移除列表指定位置的值，并返回该值 | `mylist.pop(1)`, `mylist.pop()` 没指定位置 则默认删除最后一个元素 ， **有返回值**
clear() | 清空列表所有的元素 | `mylist.clear()`


例子

```python
mylist = ['A', 'B', 'C', 'D', 'A', 'C']
del mylist[1]
print(mylist)

mylist.remove('C')
print(mylist)

mylist.pop(2)
print(mylist)

mylist.pop()
print(mylist)

mylist.clear()
print(mylist)
```





```