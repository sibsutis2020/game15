from variables import *
from tkinter import *

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
def create_elem( elem_num):
    el = elems[elem_num]
    row_num = elem_num // 4
    col_num = elem_num % 4
    color_num = int(el[1:])
    elem_color = colors[color_num]
    x_left = col_num * cell_size
    y_top = row_num * cell_size
    canv.create_rectangle(x_left + 1, y_top + 1, x_left + cell_size - 2, y_top + cell_size - 2,
            fill = elem_color, outline="#050", width = 2, tag = el)
    canv.create_text(x_left + 30, y_top + 30, text = el[1:], font = ("Arial", 20), tag = "t"+el)

#отрисовка элементов
def draw_elem( elem_num):
    el = elems[elem_num]
    row_num = elem_num // 4
    col_num = elem_num % 4
    color_num = int(el[1:])
    elem_color = colors[color_num]
    x_left = col_num * cell_size
    y_top = row_num * cell_size
    canv.coords(el, x_left + 1, y_top + 1 , x_left + cell_size - 2, y_top + cell_size - 2 )
    canv.coords("t"+el, x_left + 30, y_top + 30 )

#прорисовка клеток
for x_num in range(x_count):
    for y_num in range(y_count):
        canv.create_line(0, y_num * cell_size, canv_width, y_num * cell_size)
        canv.create_line( x_num * cell_size, 0, x_num * cell_size, canv_height)
