#параметры поля
cell_size = 60
x_count = 4
y_count = 4

#статус игры
game_status = -1

#массив игровых элементов
elems = ["e1", "e2", "e3","e4","e5","e6","e7","e8", "e9","e10","e11", "e12","e13","e14","e15","e0"]

#массив цветов элементов
a = 0
colors = ["black"]
while a < 15:
    colors.append("skyblue")
    a += 1

#формирование канавы
canv_width = x_count * cell_size
canv_height = y_count * cell_size

temp = 0
after_id = ''

temp0 = 1
