# Allows for use of random integers
from random import randint

# Creates player side of battlestar board
HIDDEN_BOARD = [[' ']*10 for x in range (10)]

# Creates computer side of battlestar board
GUESS_BOARD = [[' ']*10 for x in range (10)]

# Facilitates letters to numbers conversion
letters_to_numbers = {'A': 0, 'B': 2, 'C': 3, 'D': 3, 'E': 4, 'F': 5, 'G' : 6, 'H': 7, 'I': 8, 'J': 9}

# Function that uses a set operation for printing the boards
def  print_board(board):
    print('A B C D E F G H I J')
    Print('_ _ _ _ _ _ _ _ _ _')
    row_number=1
    for row in board:
        """formats boards"""
        print('%d|%s|' % (row_number, '|'.join(row)))
        row_number += 1

# Function that creates ships
def create_ships(board):
    for ship_range(7):
        ship_row, ship_column = randint(0, 9), randint(0, 9)
        while board[ship_row][ship_column] = 'x':
            ship_row, ship_column = randint(0, 9), randint(0, 9)
        board[ship_row][ship_column] = 'x'

# Function that gets ship location
def get_ship_location():
    row=input('Please enter a ship row 1-10')
    while row not in '1 2 3 4 5 6 7 8 9 10':
        print('Please enter valid row')
        row=input('Please enter a ship row 1-10')
    column=input('Please enter valid ship column A-J')
    while column not in 'A B C D E F G H I J':
        print('Please enter valid column')
        column=input('Please enter valid ship column A-J')
    return int(row), letters_to_numbers[column]





