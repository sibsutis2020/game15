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

root = Tk()
root.title("Пятнашки")

canv = Canvas(root, width = canv_width, height = canv_height)
canv.pack()

root.mainloop()
