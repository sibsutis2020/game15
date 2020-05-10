from tkinter import *
import random
from datetime import datetime

#параметры поля
cell_size = 60
x_count = 4
y_count = 4

#статус игры
game_status = -1

#массив игровых элементов
elems = ["e1", "e2", "e3","e4","e5","e6","e7","e8", "e9","e10","e11", "e12","e13","e14","e15","e0"]

#формирование канавы
canv_width = x_count * cell_size
canv_height = y_count * cell_size


#перемешивание элементов | рестарт
def reshuffle():
    global elems, game_status, temp
    game_status = 0
    random.shuffle(elems)
    for el_num in range(len(elems)):
        draw_elem(el_num)
    temp = 0

#секундомер
temp = 0
after_id = ''
def tick():
    global temp, after_id
    after_id = root.after(1000, tick)
    f_temp = datetime.fromtimestamp(temp).strftime("%M:%S")
    time.configure(text=str(f_temp))
    temp += 1

#функция старта игры
def start():
    global game_status, elems, time, step

    step = Label(root, width=5, font=("Ubuntu", 15), text="0")
    step.pack()

    time = Label(root, width=5, font=("Ubuntu", 15), text="00:00")
    time.pack()

    if game_status == -1 :  #начать игру в первый раз
        random.shuffle(elems)
        for el_num in range(len(elems)):
            create_elem(el_num)
    elif game_status == 1:  #начать игру заново
        random.shuffle(elems)
        for el_num in range(len(elems)):
            draw_elem(el_num)
    game_status = 0

    greeting.pack_forget()

    start.pack_forget()

    restart = Button(f_bottom, text = "Restart", font = ("Ubuntu", 13), bg = "skyblue", width = 10, command = reshuffle, )
    restart.pack(side = LEFT)

    tick()

root = Tk()
root.title("Пятнашки")

f_top = Frame()
f_top.pack()

canv = Canvas(root, width = canv_width, height = canv_height)
canv.pack()

f_bottom = Frame()
f_bottom.pack(side = BOTTOM, fill = X)

#создание элементов
def create_elem(el_num):
    el = elems[el_num]
    row_num = el_num // 4
    col_num = el_num % 4
    x_left = col_num * cell_size
    y_top = row_num * cell_size
    canv.create_rectangle(x_left + 1, y_top + 1, x_left + cell_size - 2,
                          y_top + cell_size - 2, fill = "skyblue", outline = "#050",
                          width = 2, tag = el)
    canv.create_text(x_left + 30, y_top + 30, text = el[1:], font = ("Arial", 20), tag = "t" + el)

#отрисовка элементов
def draw_elem(el_num):
    el = elems[el_num]
    row_num = el_num // 4
    col_num = el_num % 4
    x_left = col_num * cell_size
    y_top = row_num * cell_size
    canv.coords(el, x_left + 1, y_top + 1 , x_left + cell_size - 2,
                y_top + cell_size - 2)
    canv.coords("t" + el, x_left + 30, y_top + 30 )

#прорисовка клеток
for x_num in range(x_count):
    for y_num in range(y_count):
        canv.create_line(0, y_num * cell_size, canv_width, y_num * cell_size)
        canv.create_line( x_num * cell_size, 0, x_num * cell_size, canv_height)

#поменять местами 2 элемента
def change_elems(el_num1, el_num2):
    elems[el_num1], elems[el_num2] = elems[el_num2], elems[el_num1]
    draw_elem(el_num1)
    draw_elem(el_num2)

#шаги
temp0 = 0
def shagi():
    global temp0, step
    f_temp0 = temp0
    step.configure(text=str(temp0))
    temp0 += 1

#проверика на завершение игры
def test_win( ):
    for el_num in range(15):
        el = elems[el_num]
        if el_num + 1 != int(el[1:]):
            return 0
    return 1

#получение списка соседних ячеек
def neighbor_cell(el_num):
    near_cells = []
    row_num = el_num // 4
    col_num = el_num % 4

    if col_num > 0:
        tmp_num = col_num + row_num * 4 - 1
        near_cells.append(tmp_num)
    if col_num < 3:
        tmp_num = col_num + row_num * 4 + 1
        near_cells.append(tmp_num)
    if row_num > 0:
        tmp_num = col_num + (row_num -1) * 4
        near_cells.append(tmp_num)
    if row_num < 3:
        tmp_num = col_num + (row_num + 1) * 4
        near_cells.append(tmp_num)
    return near_cells

def close():
    root.destroy()

#сдвиг элементов
def test_elems(event):
    global game_status
    if game_status:
        return
    #номер элемента
    col_num = event.x // cell_size
    row_num = event.y // cell_size
    el_num = col_num + row_num * 4

    el = elems[el_num]
    #щелчок по пустому полю
    if el == "e0":
        return

    #ячейки-соседи
    near_cells = neighbor_cell(el_num)

    #проверить ячейки-соседи на 0
    for tmp_num in near_cells:
        if elems[tmp_num] == "e0":
            change_elems(el_num, tmp_num)
            shagi()
            game_status = test_win()
    return

#привязка к событиям мыши
canv.bind("<Button-1>", test_elems)

greeting = Label(f_top, text = "Hello, Player!", font = ("Ubuntu", 20))
greeting.pack()

start = Button(f_bottom, text = "Start", font = ("Ubuntu", 13), bg = "skyblue", width = 10, command = start)
start.pack(side = LEFT)

close = Button(f_bottom, text = "Close game", font = ("Ubuntu", 13), bg = "skyblue", command = close)
close.pack(side = RIGHT)

root.mainloop()
