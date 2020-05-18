from tkinter import *
import random
from datetime import datetime
from tkinter.messagebox import *
from variables import *
from neighbor_cell import *

#вывод диалогового окна при победе
def win_window():
    w_w = askyesno("", "ВЫ ПОБЕДИЛИ!!!\n" +"Время игры: " + str(temp)+ " sec\n" + "Кол-во шагов: "+ str(temp0 - 1) +
    "\nХотите начать заново?")

    if w_w == 0:
        close()
    elif w_w == 1:
        reshuffle()

#перемешивание элементов | рестарт
def reshuffle():
    global elems, game_status, temp, temp0
    game_status = 0
    random.shuffle(elems)
    for el_num in range(len(elems)):
        draw_elem(el_num)
    root.after_cancel(after_id)

    temp0 = 0
    step.configure(text=str(temp0))
    temp = 0
    time.config(text = "00:00")

    shagi()
    tick()

#секундомер
def tick():
    global temp, after_id
    after_id = root.after(1000, tick)
    f_temp = datetime.fromtimestamp(temp).strftime("%M:%S")
    time.configure(text=str(f_temp))
    temp += 1

    if game_status == 1:
        root.after_cancel(after_id)

#функция старта игры
def start():
    global game_status, elems, time, step

    step = Label(f_top, width=5, font=("Ubuntu", 15), text="0")
    step.pack(side = RIGHT)

    time = Label(f_top, width=5, font=("Ubuntu", 15), text="00:00")
    time.pack(side = LEFT)

    if game_status == -1 :  #начать игру в первый раз
        random.shuffle(elems)
        for el_num in range(len(elems)):
            create_elem(el_num)
    game_status = 0

    greeting.pack_forget()

    start.pack_forget()

    restart = Button(f_bottom, text = "Restart", font = ("Ubuntu", 13), bg = "skyblue", width = 10, command = reshuffle, )
    restart.pack(side = LEFT)

    tick()

root = Tk()
root.title("Пятнашки")
root.resizable(False, False)

f_top = Frame()
f_top.pack(fill = X)

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
def shagi():
    global temp0, step
    step.configure(text=str(temp0))
    temp0 += 1

#проверика на завершение игры
def test_win( ):
    for el_num in range(15):
        el = elems[el_num]
        if el_num + 1 != int(el[1:]):
            return 0
    return 1

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
            if game_status:
                win_window()
    return

#привязка к событиям мыши
canv.bind("<Button-1>", test_elems)

greeting = Label(f_top, text = "Hello, Player!", font = ("Ubuntu", 20))
greeting.pack()

start = Button(f_bottom, text = "Start", font = ("Ubuntu", 13), bg = "skyblue", width = 10, command = start)
start.pack(side = LEFT)

exit = Button(f_bottom, text = "Close game", font = ("Ubuntu", 13), bg = "skyblue", command = close)
exit.pack(side = RIGHT)

root.mainloop()
