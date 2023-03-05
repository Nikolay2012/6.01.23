import modules.choice_action as m_action
import modules.win_lose as m_win_lose

def click_cell(x,y):
    if y > 0 and y < 100:
        # Створюємо умову для першої комірки 
        if x < 0 and x > -100:
            m_action.players_choice_move(-100, 100, 0)  
        # Створюємо умову для другої комірки 
        elif x > 0 and x < 100:
            m_action.players_choice_move(0, 100, 1)
        # Створюємо умову для третьої комірки 
        elif x > 100 and x < 200:
            m_action.players_choice_move(100, 100, 2)
        m_win_lose.horizontal_victory(value = 1, x = -50, y = 50, start = 0, stop = 3)
        m_win_lose.horizontal_victory(value = 2, x = -50, y = 50, start = 0, stop = 3)
    elif y < 0 and y > -100:
        # Створюємо умову для четвертої комірки
        if x < 0 and x > -100:
            m_action.players_choice_move(-100, 0, 3)
        # Створюємо умову для п'ятої комірки
        elif x > 0 and x < 100:
            m_action.players_choice_move(0, 0, 4)
        # Створюємо умову для шостої комірки
        elif x > 100 and x < 200:
            m_action.players_choice_move(100, 0, 5)
        m_win_lose.horizontal_victory(1, -50, -50, 3, 6)
        m_win_lose.horizontal_victory(2, -50, -50, 3, 6)
    elif y < -100 and y > -200:
        # Створюємо умову для сьомої комірки
        if x < 0 and x > -100:
            m_action.players_choice_move(-100, -100, 6)
        # Створюємо умову для восьмої комірки
        elif x > 0 and x < 100:
            m_action.players_choice_move(0, -100, 7)
        # Створюємо умову для дев'ятої комірки
        elif x > 100 and x < 200:
            m_action.players_choice_move(100, -100, 8)
        m_win_lose.horizontal_victory(1, -50, -150, 6, 9)
        m_win_lose.horizontal_victory(2, -50, -150, 6, 9)
    m_win_lose.vertical_victory(value = 1, start= 0, x = -50, y = 50 )
    m_win_lose.vertical_victory(value = 2, start= 0, x = -50, y = 50 )
    m_win_lose.vertical_victory(value = 1, start= 1, x = 50, y = 50 )
    m_win_lose.vertical_victory(value = 2, start= 1, x = 50, y = 50 )
    m_win_lose.vertical_victory(value = 1, start= 2, x = 150, y = 50 )
    m_win_lose.vertical_victory(value = 2, start= 2, x = 150, y = 50 )