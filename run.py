    

"""The BattleBoard class is called to create the player_boards, created and implemented in the GameLogic class"""
class BattleBoard:
    """Creates Board"""
    def __init__(self) :
        self.board=[['']*8 for _ in range(8)]

    def print_board(self, hide_ships=False):
        """Prints Board"""
        print(' 12345678')
        print(' ********')
        row_num=1
        for row in self.board:
            print("%d|%s"%(row_num,"|".join(self.hide_ships(row) if hide_ships else row)))
            row_num +=1

    def hide_ships(self, row):
        """Hide opponent's ship placement"""
        return [' ' if cell == 'x'else cell for cell in row]



"""The Player class handles the manual placement of ships for each player and tests for value errors."""
class Player:
    """Creates Player"""
    def __init__(self,name):
        self.name=name
        self.board=BattleBoard()


    def place_ships(self):
        """Allows manual placement of ships"""
        print(f'{self.name}, place your ships:')
        for _ in range(5):
            row, col=self.get_ship_coordinates()
            while self.board.board[row][col]=='x':
                print('You already placed a ship there. Choose a different location.')
                row, col=self.get_ship_coordinates()
            self.board.board[row][col]='x'


    def get_ship_coordinates(self):
        """Get ship coordinates from player"""
        try:
            row=int(input('Enter the row coordinate (1-8): '))-1
            col=int(input('Enter the column coordinate (1-8): '))-1

            if not (0 <= row < 8) or not (0 <= col < 8):
                print('Invalid coordinates. Try again.')
                return self.get_ship_coordinates()

            return row, col

        except ValueError:
            print('Invalid input. Please enter numbers. Try again.')
            return self.get_ship_coordinates()


    def attack(self, target_player):
        """Player attacks target player board"""
        target_player_board=target_player.board
        target_player_board.print_board(hide_ships=True)

        try:
            row=int(input(f'{self.name}, choose a row to attack (1-8): '))-1
            col=int(input(f'{self.name}, choose a column to attack (1-8)'))-1

            if not (0 <= row < 8) or not (0 <= col < 8):
                print('Invalid coordinates. Try again')
                return self.attack(target_player)

            if target_player.board.board[row][col]=='x':
                print(f'{self.name} hit the target!')
                target_player.board.board[row][col]='H'

            else:
                print(f'{self.name} hit the target!')
                target_player.board.board[row][col]=M

        except ValueError:
            print('Invalid input. Please enter numbers. Try again')
            return self.attack(target_player)


"""The GameLogic class defines the two players, calls the place_ships method, handles player turn alternation and tests for game over."""
class GameLogic:
    """Creates game logic, assigns players 1&2"""
    def __init__(self):
        self.players=[Player('Player 1'), Player('Player 2')] 


    def run_game(self):
        for player in self.players:
            player.place_ships()

        current_player_index=0

        while True:
            attacking_player=self.players[current_player_index]
            target_player=self.players[1-current_player_index]
            attacking_player.attack(target_player)

            if self.is_game_over():
                print(f'{attacking_player.name} wins!')
                break

            current_player_index=1-current_player_index


    def is_game_over(self):
        for player in self.players:
            if all(cell != 'x' for row in player.board.board for cell in row):
                return True
        return False

    

if __name__=='__main__':
    game_logic=GameLogic()
    game_logic.run_game()