import turtle

t3 = turtle.Turtle()
t3.width(3)
t3.color("blue")
t3.speed(0)
t3.hideturtle()

def make_zero(x, y):
    t3.penup()
    t3.goto(x, y)
    t3.pendown()
    t3.circle(50)
