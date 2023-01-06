import turtle 

t2 = turtle.Turtle()
t2.width(3)
t2.color("red")
t2.speed(0)
t2.hideturtle()

def cross(x, y):
    x_cor = x
    y_cor = y
    step = 100
    for count in range(2):
        t2.penup()
        t2.goto(x_cor, y_cor)
        t2.pendown()
        t2.goto(x_cor + step, y_cor - 100)
        x_cor += 100
        step *= -1

