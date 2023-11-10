class BattleBoard:
"""The BattleBoard class is called to create the player_boards, created and implemented in the GameLogic class"""
    def__init__(self):
        self.board=[['']*8 for_in range(8)]

    def print_board(self):
        print(' 12345678')
        print(' ********')
        row_num=1
        for row in self.board:
            print("%d|%s"%(row_num,"|".join(row)))
            row_num +=1


class Player:
    """The Player class handles the manual placement of ships for each player and tests for value errors."""
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
        """Get ship 

    