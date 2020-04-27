from tkinter import *

#параметры поля
cell_size = 60
x_count = 4
y_count = 4

#массив игровых элементов
elems = ["e1", "e2", "e2","e3","e4","e5","e6","e7", "e8","e8","e9","e10","e11", "e12","e13","e14","e15","e0"]

#формирование канавы
canv_width = x_count * cell_size
canv_height = y_count * cell_size


#функция с удалением приветствия
def start():
    f_top.pack_forget()

    for el_num in range(len(elems)):
        create_elem(el_num)

root = Tk()
root.title("Пятнашки")

f_top = Frame()
f_top.pack()

canv = Canvas(root, width = canv_width, height = canv_height)
canv.pack()

#создание элементов
def create_elem(el_num):
    el = elems[el_num]
    row_num = el_num / 4
    col_num = el_num % 4
    x_left = col_num * cell_size
    y_top = row_num * cell_size
    canv.create_rectangle(x_left + 1, y_top + 1, x_left + cell_size - 2,
                          y_top + cell_size - 2, fill = "skyblue", outline = "#050",
                          width = 2, tag = el)
    canv.create_text(x_left + 30, y_top + 30, text = el[1:], font = ("Arial", 20), tag = "t" + el)

#прорисовка клеток
for x_num in range(x_count):
    for y_num in range(y_count):
        canv.create_line(0, y_num * cell_size, canv_width, y_num * cell_size)
        canv.create_line( x_num * cell_size, 0, x_num * cell_size, canv_height)

greeting = Label(f_top, text = "Hello, Player!", font = ("Ubuntu", 20))
greeting.pack()

start = Button(text = "Start", font = ("Ubuntu", 15), bg = "skyblue", command = start)
start.pack()

root.mainloop()
