import turtle

def curvemove():
    """绘制心形曲线的一部分"""
    for _ in range(100):  # 减少循环次数
        turtle.right(2)  # 增大旋转角度
        turtle.forward(2)  # 墛大前进距离

def draw_heart():
    """绘制完整的心形"""
    turtle.color('red')
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(111.65)
    curvemove()
    turtle.left(120)
    curvemove()
    turtle.forward(111.65)
    turtle.end_fill()

def main():
    """主函数，设置画布并绘制心形"""
    turtle.speed(0)  # 设置最快速度
    turtle.penup()
    turtle.goto(0, -70)
    turtle.pendown()
    draw_heart()
    turtle.penup()
    turtle.goto(-40, -50)
    turtle.pendown()
    turtle.hideturtle()
    turtle.done()  # 保持窗口打开

if __name__ == "__main__":
    main()