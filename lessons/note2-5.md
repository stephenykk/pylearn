# python的基础语法

## 数据类型

### 布尔类型(boolean)
布尔类型只有真值和假值，真值用**True**表示，假值用**False**表示。

> 布尔类型的值也可以当作数值来用，True 看作 1, False 看作 0
> ```python
> a = 100 + True
> print(a) # 101
> a = 100 * False
> print(a) # 0
> ```

例子
```python
a = 10
b = 11
print(a > b) # False
print(a < b) # True
```
## 逻辑运算
逻辑运算是对布尔值进行运算，结果还是布尔值(*True / False*)

布尔运算符表
布尔运算符 | 描述 | 例子  | 解释
|:-------:|:------:|:-------:|:-----|
and  | “与”运算 | x and y  | x 和 y 都为True时，结果才为True; 否则结果为False
or | “或”运算 | x or y | x 或 y 只要有一个为True, 结果就为True; 只有 x 和 y 都不为True时，结果才为False
not | “非"运算 | not x | 反转逻辑值，x为True, 结果为False; x为False, 结果为True

例子
```python
value1 = input('请输入数字(1 代表下雨, 0  代表不下雨): ')
value2 = input('请输入数字(1 代表有作业, 0 代表没作业): ')

rainy = int(value1) > 0 # True or False
buzy = int(value2) > 0 # True or False

if rainy or buzy:
    print('我只能呆在家里:(')

if not rainy and not buzy:
    print('我可以去公园玩:)')

if not buzy:
    print('我有空，可以在家看电视或去公园玩')

```

## 运算符优先级
数学运算中，有”先乘除，后加减“的规则(`如: 2 + 3 * 4`)，意思就是乘/除法比加/减法优先计算，这就是运算符的优先级

```python
'''
因为 * 比 + 优先级高，所以
1. 先算 3 * 4 得到 12
2. 再算 2 + 12 得到 14
'''
result = 2 + 3 * 4 # 14
```
数学里，只有算术运算符 **+ - * / %**，大家都是算术运算符，但它们之间也有优先级，规则就是 "先乘除，后加减法"

python里，有多种类型的运算符：算术运算符、比较运算符和逻辑运算符。

```python
a = 5 + 2 * 4  # 算术运算符
b = a > 10 # 比较运算符
c = a < 20 
d = b and c # 逻辑运算符  
```

不同类型运算符的优先级不同，优先级从高到低为: **算术运算符 > 比较运算符 > 逻辑运算符**

> 为什么是这个优先顺序呢？  
> 观察上面的例子  
> 1. 逻辑运算需要布尔值(True / False),  
> 比较运算才能产生布尔值，所以先进行比较运算，   
> **因此，有优先级：比较运算符 > 逻辑运算符**
> 2. 比较运算需要数值，  
> 算术运算才能产生数值，所以先进行算术运算  
> **因此，有优先级: 算术运算符 > 比较运算符**

```python
# 下面表达式包含了几种类型的运算符？
# 分析它的计算顺序
result = 3 * 4 > 10 and 2 + 6 < 7
print(result) # False
```

数值运算例子
```python
# 整数 + 整数 结果为整数
4 + 5 # 9

# 整数 + 浮点数 结果为浮点数
# 浮点数即带小数点的数
3 + 2.0 # 5.0

# 查看类型的方法
# type(value) # type是函数， value是参数
value = 2.4
print(type(value))
```

## 练习
1. 先思考，再实践
    ```python
    x = 4
    x *= 6
    print(x) # 结果为?
    ```
2. 先思考，再实践
   ```python
   print(3 === 4 or 5 > 2) # 结果为?
   print(5 >= 5 and 7 < 8) # 结果为?
   ```
3. 抄写并运行下面程序
   ```python
   # coding: utf-8
   print('自动判断正负数程序')

   value = input('请输入一个数字: ')
   value = int(value)
   
   print('你输入的是:')

   if value > 0:
       print('正数')
   elif value < 0:
       print('负数')
   else:
       print('零')
 
    ```