import turtle

t1 = turtle.Turtle()
t1.hideturtle()
t1.speed(0)
t1.width(3)

def create_table(x, y):
    x_cor = x 
    y_cor = y
    for count2 in range(3):
        for count1 in range(3): 
            count = 0
            t1.penup()
            t1.goto(x_cor, y_cor)
            t1.pendown()
            while count < 4:   
                t1.forward(100)
                t1.left(90)
                count += 1
            x_cor = x_cor + 100
        x_cor = x_cor - 300
        y_cor = y_cor - 100
        t1.penup()
        t1.goto(x_cor, y_cor)
        t1.pendown()



 
    
    
