import turtle

def curvemove():
  for i in range(200):
    turtle.right(1)
    turtle.forward(1)

turtle.penup()
turtle.goto(0, -70)
turtle.pendown()

turtle.color('red')
turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)
curvemove()
turtle.left(120)
curvemove()
turtle.forward(111.65)
turtle.end_fill()

turtle.penup()
turtle.goto(-40, -50)
turtle.pendown()
turtle.hideturtle()

turtle.done()  # 保持窗口打开