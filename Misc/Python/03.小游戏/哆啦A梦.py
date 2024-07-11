import turtle

# 创建哆啦A梦
doraemon = turtle.Turtle()
doraemon.speed(10)

def draw_eye_white_circle(x):
  doraemon.goto(x, 80)
  doraemon.pendown()
  doraemon.color('black')
  doraemon.begin_fill()
  doraemon.circle(15)
  doraemon.color('white')
  doraemon.end_fill()

def draw_eye_black_circle(x):
  doraemon.goto(x, 90)
  doraemon.color('black')
  doraemon.begin_fill()
  doraemon.begin_fill()
  doraemon.circle(6)
  doraemon.end_fill()
  doraemon.penup()

# 画蓝色圆
doraemon.color('#0093dd')
doraemon.begin_fill()
doraemon.circle(60)
doraemon.end_fill()

# 画白色圆
doraemon.begin_fill()
doraemon.circle(50)
doraemon.color('white')
doraemon.end_fill()

# 画右眼白
draw_eye_white_circle(15)

# 画右眼黑
draw_eye_black_circle(6)

# 画左眼白
draw_eye_white_circle(-15)

# 画左眼黑
draw_eye_black_circle(-24)

# 画鼻子
doraemon.goto(0, 60)
doraemon.pendown()
doraemon.color('#c70000')
doraemon.begin_fill()
doraemon.circle(8)
doraemon.end_fill()

doraemon.color('black')
# 设置朝向（对应上北下南，左西右东）
# 0 为东，90 为北，180 为西，270 为南（同 -90）
doraemon.setheading(-90)
# 沿着刚刚设定的朝下方向绘制 40px
doraemon.forward(40)
doraemon.penup()

# 画嘴巴
doraemon.goto(-30, 40)
doraemon.pendown()
doraemon.circle(30, 180)
doraemon.penup()
doraemon.goto(0, 0)