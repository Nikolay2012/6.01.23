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
    t4.goto(x + 200, y)

def draw_line_vertical(x, y):
    t4.penup()
    t4.goto(x,y)
    t4.pendown()
    t4.goto(x, y - 200)

def horizontal_victory(value, x, y, start, stop):
    count_victory = 0
    for number in range(start, stop):
        if m_data.list_cell[number] == value:
            count_victory += 1
    if count_victory == 3:
        draw_line(x, y)
        m_data.step[0] = ''
        
def vertical_victory(value, start, x, y):
    count_victory = 0
    for number in range(3):
        if m_data.list_cell[start] == value:
            count_victory += 1
            start = start + 3
    if count_victory == 3:
        draw_line_vertical(x, y)
        m_data.step[0] = ''
        
