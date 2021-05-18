# turtle库综合应用

turtle库结合变量、循环和分支结构可以绘制复杂的图形

## 与for循环结合

绘制五角星

```python
import turtle as t
for i in range(5):
    t.forward(200)
    t.right(144)
t.done()
```

### 与while循环结合

同样绘制五角星 

```python
import turtle as t
i = 0
while i < 5:
    t.forward(200)
    t.right(144)
    i += 1
t.done()
```


### 与分支结构结合

带颜色的五角星

```python
import turtle as t
t.pensize(5) # 设置画笔大小
t.hideturtle() # 隐藏画笔
for i in range(5):
    if i % 2 == 0:
        t.pencolor('orange')
    else:
        t.pencolor('green')
    t.forward(200)
    t.right(144)
t.done()
```


## 练习
1. 六角花

```python
import turtle as t
t.speed(1)
t.left(90)

for m in range(6):
    for i in range(6):
        t.forward(80)
        t.left(60)
    t.left(60)
t.done()
```

2. 类旋转风车图形

```python
import turtle as t
t.speed(1)
t.pencolor('green')

for i in range(4):
    for m in range(4):
        if m % 2 == 0:
            t.forward(120)
        else:
            t.forward(60)
        t.left(90)
    t.left(90)
t.done()

```
