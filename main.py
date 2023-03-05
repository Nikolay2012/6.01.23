import turtle
import modules.create_screen as m_screen
import modules.table_creation as m_table
import modules.click_handler as m_click
#
m_table.create_table(-100, 0)
m_screen.screen.onclick(m_click.click_cell, btn= 1, add= True)
# 
turtle.done()





