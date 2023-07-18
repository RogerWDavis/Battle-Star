# Allows for use of random integers
from random import randint


class BattleBoard:
    """Creates Board"""
    def __init__(self, board):
        self.board = board

    def print_board(self):
        """prints board"""
        print('   1 2 3 4 5 6 7 8')
        print('   ***************')
        row_num = 1
        for row in self.board:
            print("%d|%s|" % (row_num, "|".join(row)))
            row_num += 1


class DeathStar:
    """Creates Ships"""
    def __init__(self, board):
        self.board = board

    def count_hit_ships(self):
        """counts successful guesses"""
        hits = 0
        for self.row in self.board:
            for self.column in self.row:
                if self.column == 'x':
                    hits += 1
        return hits

    def create_ships(self):
        """creates computer targets"""
        for i in range(5):
            self.row, self.column = randint(0, 7), randint(0, 7)
            while self.board[self.row][self.column] == 'x':
                self.row, self.column = randint(0, 7), randint(0, 7)
            self.board[self.row][self.column] = 'x'
        return self.board


def get_user_input():
    """gets user inputs"""
    try:
        row = input('Please enter a row coordinate 1-8: ')
        while row not in '12345678':
            row = input('Please enter a valid row 1-8: ')

        column = input('Please enter column coordinate 1-8: ')
        while column not in '12345678':
            column = input('Please enter valid column  1-8: ')

        return int(row)-1, int(column)-1

    except ValueError:
        print("Please enter a number")
        return get_user_input()

        data_str=input("enter your data here:\n")


def GameLogic():
    """creates game logic"""
    death_star = BattleBoard([[' ']*8 for x in range(8)])
    sky_walker = BattleBoard([[' ']*8 for x in range(8)])
    DeathStar.create_ships(death_star)
    lasers = 10
    while lasers > 0:
        print('Welcome to Battle Star!')
        BattleBoard.print_board(death_star)
        BattleBoard.print_board(sky_walker)
        sky_row, sky_column = get_user_input()
        if sky_walker.board[sky_row][sky_column] == '-':
            print('You already tried that. Use the Force')
            sky_row, sky_column = get_user_input()
        elif sky_walker.board[sky_row][sky_column] == 'x':
            print('You already tried that. Use the Force')
            sky_row, sky_column = get_user_input()
        elif death_star.board[sky_row][sky_column] == 'x':
            print('Hit! The Force is strong with you')
            sky_walker.board[sky_row][sky_column] = 'x'
            lasers -= 1
        else:
            print('Miss! Try again. Use the Force.')
            sky_walker.board[sky_row][sky_column] = '-'
            lasers -= 1
        if DeathStar.count_hit_ships(sky_walker) == 5:
            print('Congratulations! You destroyed the Death Star!')
            break
        print(f'you have  {lasers} lasers remaining')
        if lasers == 0:
            print('Game Over')
            break


if __name__ == '__main__':
    GameLogic()







