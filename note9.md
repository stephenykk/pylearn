# python标准库入门

什么是turtle(*海龟*)?  
turtle是一个直观有趣的图形绘制函数库。  

> turtle是内置在python中的 无需安装

turtle库中有一支神奇的画笔，从绘画窗口正中心开始，根据指令在画布上游走。  

我们可以控制画笔的颜色，粗细和方向，从而绘制多彩的图形  

本课将介绍turtle库中基本函数的运用

## 基本画笔控制函数

函数  |  说明
---- | -----
forward() | 画笔前进
left() | 画笔左转
right() | 画笔右转
goto() | 画笔移动到指定坐标位置
penup() | 抬笔
pendown() | 落笔

### forward()函数

语法: `turtle.forward(distance)`

- distance 距离，表示前进多长距离，单位为像素，可以为负数，即表示倒退

例子

```python
import turtle # 引入turtle库
turtle.forward(100) # 画笔前进100像素
turtle.done() # 停止绘制，但是绘图窗体不关闭
```

### left()函数

语法: `turtle.left(angle)`
- angle 角度，画笔左转多少度，可以为负数角度 即右转
 
例子

```python
import turtle
turtle.forward(100)
turtle.left(90)
turtle.forward(100) # 画笔左转90度
turtle.done()
```

### right()函数
语法： `turtle.right(angle)`
- angle 角度, 画笔右转多少度  可以为负数角度，即左转

例子


```python
import turtle
turtle.forward(100)
turtle.right(90)
turtle.forward(100) # 画笔右转90度
turtle.done()
```

### goto()函数

语法：`turtle.goto(x, y)`

控制画笔移动到指定坐标

```python
import turtle
turtle.goto(100, 100)
turtle.done()
```

### penup()函数
抬笔，移动时不会绘制线条

语法: `turtle.penup()`

```python
import turtle
turtle.penup()
turtle.forward(100)
turtle.done()
```
### pendown()函数
落笔，常与`penup()`函数成对使用

语法: `turtle.pendown()`

例子

```python
import turtle
turtle.forward(50)
turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.forward(50)
turtle.done()
```

## 设置画笔属性的函数

turtle设置画笔属性的函数主要有:

函数  |  说明
--- | ---
pensize()  | 设置画笔大小
pencolor() | 设置画笔颜色
speed()  | 设置绘画速度

### pensize()函数

语法：`turtle.pensize(width)`

例子

```python
import turtle
turtle.forward(100)
turtle.pensize(10)
turtle.forward(100)
turtle.done()
```

### pencolor()函数

语法: `turtle.pencolor(color)`

例子

```python
import turtle
turtle.pencolor('red')
turtle.forward(100)
turtle.pencolor('green')
turtle.forward(100)
turtle.done()
```

### speed()函数

用来设置画笔速度

语法: `turtle.speed(speed)`

- speed 画笔速度，范围为0~10 0为最大速度， 1～10速度增加

例子 

```python
import turtle as t
t.speed(2)
for x in range(100):
    if x == 10:
        t.speed(9)
    t.forward(x)
    t.left(90)
t.done()
```

## 其他常用函数

函数  |  说明
--- | ---
hideturtle()  |  隐藏画笔
done()  | 停止绘制，但绘图窗口不会关闭

### hideturtle() 函数

语法: `turtle.hideturtle()`

例子

```python
import turtle as t
t.hideturtle() # 隐藏画笔
# 画一个三角形
for i in range(3):
    t.forward(200)
    t.left(200)
t.done()
```

### done()函数
停止画笔，并且阻止绘画窗口关闭。如果接下来还需要用到画笔，画笔也不会再启动
