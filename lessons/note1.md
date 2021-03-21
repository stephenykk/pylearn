# python 语言概述

## IPO程序的编写方法 p13
IPO(input-process-output)程序的编写方法是每个程序都具备的模式。

> 如计算面积的程序，用户需要输入长和宽的数据，程序按照面积公式做数据处理，最后输出结果给用户。

> 如导航程序，用户输入目的地，程序根据地图数据和交通状态做数据处理，最后输出导航路线给用户选择

### 输入/输出函数

#### input()函数  

- 语法: `input([prompt])`

- 例子
```python
    a = input("请输入：")
    print(a)
```

#### print()函数
- 语法： `print(message)`

- 例子
```python
a = 'hello python'
print(a)
print('ni hao a')
print(1000)
```

## 练习
- 编写一个能够输出"hello world"的python程序
