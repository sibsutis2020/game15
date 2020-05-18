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
