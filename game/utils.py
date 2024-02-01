from random import randint


def set_field_with_mines(instance, row_, col_):
    field = [["0" for i in range(int(instance.width))]
             for j in range(int(instance.height))]
    mines_positions = []
    count = 0
    while count < instance.mines_count:
        col = randint(0, instance.width - 1)
        row = randint(0, instance.height - 1)
        if (row, col) not in mines_positions and (row, col) != (row_, col_):
            field[row][col] = '-9'
            mines_positions.append((row, col))
            count += 1

    for pos in mines_positions:
        row, col = pos
        if 0 <= row - 1:
            if 0 <= col - 1:
                field[row - 1][col - 1] = str(int(field[row - 1][col - 1]) + 1)
            field[row - 1][col] = str(int(field[row - 1][col]) + 1)
            if col + 1 < instance.width:
                field[row - 1][col + 1] = str(int(field[row - 1][col + 1]) + 1)
        if 0 <= col - 1:
            field[row][col - 1] = str(int(field[row][col - 1]) + 1)
        if col + 1 < instance.width:
            field[row][col + 1] = str(int(field[row][col + 1]) + 1)
        if row + 1 < instance.height:
            if 0 <= col - 1:
                field[row + 1][col - 1] = str(int(field[row + 1][col - 1]) + 1)
            field[row + 1][col] = str(int(field[row + 1][col]) + 1)
            if col + 1 < instance.width:
                field[row + 1][col + 1] = str(int(field[row + 1][col + 1]) + 1)
    return field


def game_is_won(field, field_with_mines):
    flag = True
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] != field_with_mines[i][j] and int(field_with_mines[i][j]) >= 0:
                flag = False
    return flag


def update_field(field):
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == ' ':
                field[i][j] = 'M'
