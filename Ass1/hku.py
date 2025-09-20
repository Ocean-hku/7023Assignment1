print("----- Welcome to the drawing system ----")
print("----- I'm going to paint the seal of HKU 111 Aniversary ----")

# "#977949"
# turtle.screensize(width, height, bg) 默认大小(400,300)
# 保持窗口：turtle.done()（防止绘图窗口自动关闭）
# home()：回到原点 (0,0)，方向重置为初始状态（向右）
# penup() / pu()：抬起画笔，移动时不留下轨迹
# pendown() / pd()：放下画笔，移动时恢复轨迹
# pensize(width) / width(width)：设置画笔粗细
# pencolor(color)：设置画笔颜色（轨迹颜色）。
# 颜色可以是：颜色名称（如 "red"）、十六进制值（如 "#FF5733"）、RGB 值（需配合 colormode(255)）
# fd(distance)：向前移动指定距离（单位：像素）
# bk(distance)：向后移动指定距离
# rt(angle)：向右（顺时针）旋转指定角度（单位：度）
# lt(angle)：向左（逆时针）旋转指定角度
# begin_fill()：标记填充起始点（在绘制封闭图形前调用）
# end_fill()：标记填充结束点（图形闭合后调用，自动填充内部）
# fillcolor(color)：设置填充颜色
# hideturtle() / ht()：隐藏海龟图标（只显示轨迹）
# shape(name)：设置海龟图标形状（如 "turtle"、"circle"、"square"）
# title(title)：设置窗口标题
# circle(radius, extent=None, steps=None)
# radius 正数：向上画 负数：向下画
# extent 正数：向右画对应角度的圆弧 负数：向左画对应角度的圆弧
# turtle 绘制圆形时，并非以海龟当前位置为圆心，而是以海龟当前位置到圆心的距离为半径

from turtle import *

screen = Screen()

x_min, x_max = -210, 210  # 左右边界
y_min, y_max = -210, 210  # 上下边界

width = x_max - x_min
height = y_max - y_min

margin = 10  # 设置白边大小

screen.setup(width + margin * 2, height + margin * 2)

screen.setworldcoordinates(x_min - margin, y_min - margin, 
                          x_max + margin, y_max + margin)

screen.title("HKU 111 Aniversary")
screen.bgcolor("white")

hideturtle()
speed(15)
pensize(5)
gold ="#977949"
black = "black"

penup()
goto(0, 190)
pendown()
pencolor(gold)
begin_fill()
fillcolor(gold)
fd(25)
rt(90)
fd(170)
circle(15, 90)
fd(10)
rt(90)
fd(5)
rt(90)
fd(105)
rt(90)
fd(5)
rt(90)
fd(15)
circle(15, 90)
fd(120)
circle(15, 90)
fd(15)
rt(90)
fd(10)
rt(90)
circle(80, 46.5)
goto(10, 190)
end_fill()

penup()
home()
goto(-95, 60)
pendown()
pencolor(black)
begin_fill()
fillcolor(black)
goto(-35, 60)
goto(-35, 55)
goto(-95, 55)
goto(-95, 60)
end_fill()

penup()
home()
goto(-125, 140)
pendown()
pencolor(gold)
begin_fill()
fillcolor(gold)
fd(20)
rt(90)
fd(170)
circle(10, 90)
fd(20)
rt(90)
fd(5)
rt(90)
fd(110)
rt(90)
fd(5)
rt(90)
fd(20)
circle(10, 90)
fd(130)
circle(10, 90)
fd(20)
rt(90)
fd(5)
rt(90)
circle(85, 45)
end_fill()

penup()
home()
goto(75, 130)
pendown()
pencolor(black)
begin_fill()
fillcolor(black)
fd(70)
rt(90)
fd(5)
rt(90)
circle(30,45)
goto(75, 80)
goto(150, -25)
goto(165, -25)
goto(165, -30)
goto(70, -30)
goto(70, -25)
goto(85, -25)
goto(85, -15)
goto(40, 55)
goto(100, 110)
seth(90)
circle(15, 90)
goto(75, 125)
goto(75, 130)
end_fill()

penup()
home()
goto(10, -15)
pendown()
pencolor(gold)
begin_fill()
fillcolor(gold)
goto(25, -15)
goto(25, -150)
seth(-90)
circle(45, 90)
goto(70, -205)
seth(0)
circle(105, -62)
goto(-25, -60)
seth(90)
circle(15, 90)
goto(-55, -45)
seth(0)
circle(85, 50)
end_fill()

penup()
home()
goto(90, -45)
pendown()
pencolor(black)
begin_fill()
fillcolor(black)
fd(75)
rt(90)
fd(5)
rt(90)
fd(15)
circle(15, 90)
goto(135, -155)
seth(90)
circle(50, -90)
goto(85, -200)
circle(40, 90)
goto(125, -65)
seth(90)
circle(15, 90)
goto(90, -50)
goto(90, -45)
end_fill()




done()