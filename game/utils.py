from random import randint
from typing import List
from .models import Game


def set_field_with_mines(instance: Game, row_: int, col_: int):
    width = instance.width
    height = instance.height
    mines_count = instance.mines_count

    field = [["0" for i in range(int(width))]
             for j in range(int(height))]
    mines_positions = []
    count = 0
    while count < mines_count:
        col = randint(0, width - 1)
        row = randint(0, height - 1)
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


def game_is_won(instance: Game):
    height = instance.height
    width = instance.width
    field = instance.field
    field_with_mines = instance.field_with_mines
    flag = True

    for i in range(height):
        for j in range(width):
            if field[i][j] != field_with_mines[i][j] and int(field_with_mines[i][j]) >= 0:
                flag = False
    return flag


def zero_case(instance: Game, row: int, col: int):
    field = instance.field
    field_with_mines = instance.field_with_mines
    width = instance.width
    height = instance.height
    stack = [(row, col)]

    while stack:
        row, col = stack.pop()
        field[row][col] = field_with_mines[row][col]
        if field_with_mines[row][col] == '0':
            if 0 <= row - 1 < height:
                if 0 <= col - 1 < width:
                    if field[row - 1][col - 1] == ' ':
                        stack.append((row - 1, col - 1))
                if 0 <= col < width:
                    if field[row - 1][col] == ' ':
                        stack.append((row - 1, col))
                if 0 <= col + 1 < width:
                    if field[row - 1][col + 1] == ' ':
                        stack.append((row - 1, col + 1))
            if 0 <= row < height:
                if 0 <= col - 1 < width:
                    if field[row][col - 1] == ' ':
                        stack.append((row, col - 1))
                if 0 <= col < width:
                    if field[row][col] == ' ':
                        stack.append((row, col))
                if 0 <= col + 1 < width:
                    if field[row][col + 1] == ' ':
                        stack.append((row, col + 1))
            if 0 <= row + 1 < height:
                if 0 <= col - 1 < width:
                    if field[row + 1][col - 1] == ' ':
                        stack.append((row + 1, col - 1))
                if 0 <= col < width:
                    if field[row + 1][col] == ' ':
                        stack.append((row + 1, col))
                if 0 <= col + 1 < width:
                    if field[row + 1][col + 1] == ' ':
                        stack.append((row + 1, col + 1))


def update_field(instance: Game, symbol: str):
    height = instance.height
    width = instance.width
    field = instance.field
    field_with_mines = instance.field_with_mines

    for i in range(height):
        for j in range(width):
            if field[i][j] == ' ':
                if int(field_with_mines[i][j]) < 0:
                    field[i][j] = symbol
                else:
                    field[i][j] = field_with_mines[i][j]

