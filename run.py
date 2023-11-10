    

"""The BattleBoard class is called to create the player_boards, created and implemented in the GameLogic class"""
class BattleBoard:
    """Creates Board"""
    def__init__(self):
        self.board=[['']*8 for_in range(8)]

    def print_board(self):
        """Prints Board"""
        print(' 12345678')
        print(' ********')
        row_num=1
        for row in self.board:
            print("%d|%s"%(row_num,"|".join(row)))
            row_num +=1


"""The Player class handles the manual placement of ships for each player and tests for value errors."""
class Player:
    """Creates Player"""
    def __init__(self,name):
        self.name=name
        self.board=BattleBoard()


    def place_ships(self):
        """Alows manual placement of ships"""
        print(f'{self.name}, place your ships:')
        for_in range(5):
            row, col=self.get_ship_coordinates()
            while self.board.board[row][col]='x'


    def get_ship_coordinates(self):
        """Get ship coordinates from player"""
        try:
            row=int(input('Enter the row coordinate (1-8): '))-1
            col=int(input('Enter the column coordinate (1-8): '))-1

            if not (0 <= row < 8) or not (0 <= < 8):
                print('Invalid coordinates. Try again.')
                return self.get_ship_coordinates()

            return row, col

        except ValueError:
            print('Invalid input. Please enter numbers. Try again.')
            return self.get_ship_coordinates()





    