import modules.create_cross as m_cross
import modules.create_zero as m_zero
import modules.data_base as m_data


def players_choice_move(x, y, number):
    if m_data.step[0] == "cross" and m_data.list_cell[number] == 0:
        m_cross.make_cross(x, y)
        m_data.list_cell[number] = 1
        m_data.step[0] = "zero"
        # print(m_data.list_cell)
    elif m_data.step[0] == "zero" and m_data.list_cell[number] == 0:
        m_zero.make_zero(x + 50, y - 100)
        m_data.list_cell[number] = 2
        m_data.step[0] = "cross"
        # print(m_data.list_cell)
        