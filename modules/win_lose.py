import modules.data_base as m_data
import turtle

t4 = turtle.Turtle()
t4.color("darkgreen")
t4.speed(0)
t4.hideturtle()
t4.width(5)

def draw_line(x, y):
    t4.penup()
    t4.goto(x,y)
    t4.pendown()
    t4.forward(200)

def horizontal_victory(value, x, y, start, stop):
    count = 0
    for number in range(start, stop):
        if m_data.list_cell[number] == value:
            count += 1
    return count
    # if count == 3:
        # draw_line(x, y)

def vertical_victory(value, x, y, start):
    count_value = 0
    for number in range(3):
        if m_data.list_cell[start] == value:
            print(f"a-{start}")
            count_value += 1
            start += 3
    return count_value
    
def win(value= 0, x= 0, y= 0, start= 0, stop= 0):
    count = horizontal_victory(value, x, y, start, stop)
    count = vertical_victory(value, x, y, start)
    if count == 3:
        draw_line(x, y)



# vertical_victory(1, 1, 2, 2)