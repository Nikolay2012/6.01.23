# Імппортуємо модуль customtkinter до файлу screen_tkinter
import customtkinter
# Імпортуємо файл search_path як m_path
# Модуль search_path допомогає створит абсолютний 
# шлях до місця розташування файлу, за його ім'ям
import search_path as m_path
# Створюємо вікно головного додатку з ім'ям screen_ctk
screen_ctk = customtkinter.CTk()
# створіємо дві змінні де зберігаємо розмір 
# головного вікна додатка по ширині та висоті
app_width, app_height = 500, 500
# визначаємо розмір екрана комп'ютера по ширині
pc_screen_width = screen_ctk.winfo_screenwidth()
# визначаємо розмір екрана комп'ютера по висоті
pc_screen_height = screen_ctk.winfo_screenheight()
# задаємо розміри додатку screen_ctk та вказуемо кордината місця розташування додатку на екрані комп'ютера
screen_ctk.geometry(f"{app_width}x{app_height}+{pc_screen_width // 2 - app_width // 2}+{pc_screen_height // 2 - app_height // 2}")
# забороняемо додатку screen_ctk змінюваати розміри ширини і висоти
screen_ctk.resizable(False, False)
# задемо заголовок додатку screen_ctk 
screen_ctk.title("Оберіть варіант гри")
# Створюємо змінну font в якій зберігаємо налаштування шрифта для тексту
font = customtkinter.CTkFont(family= "Arial", size= 18, weight= "bold")
# Задаємо напис над полем ввода імені гравця
label_plaeyr1 = customtkinter.CTkLabel(master= screen_ctk, text="Задайте ім'я першого гравця", font= font)
label_plaeyr2 = customtkinter.CTkLabel(master= screen_ctk, text="Задайте ім'я другого гравця", font= font)
# Створюємо змінну dict1 з типом даних словник
dict1 = dict()
# Створюємо змінну input_text_player1 для запису імені першого гравця
input_text_plaeyr1= customtkinter.CTkEntry(
    master= screen_ctk, # У параметрі master вказуємо назву додатку у якому розміщується input_text_plaeyr1=
    width= 300, 
    height= 50, 
    border_width= 2,
    border_color= "orange",
    placeholder_text= "Задайте ім'я",
    font = font,
    text_color= "orange"
)
#
input_text_plaeyr2 = customtkinter.CTkEntry(
    master=screen_ctk, 
    width= 300, 
    height= 50, 
    border_width= 2,
    border_color= "orange",
    placeholder_text= "Задайте ім'я",
    font= font,
    text_color= "orange"
)
# Створюємо функцію що зберігає дані та виконує запис імені першого та другого гравця у файл json
def save_text():
    dict1["name1"] = input_text_plaeyr1.get()
    dict1["name2"] = input_text_plaeyr2.get()
    m_path.dump_json("json/GAME1.json", dict1)
    # 
    input_text_plaeyr1.delete(0, customtkinter.END)
    input_text_plaeyr2.delete(0, customtkinter.END)
# Створюмо кнопку що буде застосовувати функцію save_text, що зберігає дані гравця
button_input = customtkinter.CTkButton(
    master=screen_ctk, 
    width= 100, 
    height=50, 
    text="OK", 
    command= save_text,
    fg_color= "darkorange",
    hover_color= "Coral"
    # bg_color= "orange"
)
# розташовуємо змінні за кординатами на єкрані додатку 
button_input.place(x= app_width // 2, y = app_height // 2 + 160, anchor= customtkinter.CENTER)
input_text_plaeyr1.place(x= app_width // 2, y = app_height // 2, anchor= customtkinter.CENTER)
input_text_plaeyr2.place(x= app_width // 2, y = app_height // 2 + 100, anchor= customtkinter.CENTER)
label_plaeyr2.place(x= app_width // 2, y = app_height // 2 + 50, anchor= customtkinter.CENTER)
label_plaeyr1.place(x= app_width // 2, y = app_height // 2 - 50, anchor= customtkinter.CENTER)
#тримає додаток відкритим.
screen_ctk.mainloop()