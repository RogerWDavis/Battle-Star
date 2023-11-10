# Allows for use of random integers
from random import randint

class BattleBoard:
"""The BattleBoard class is called to create the player_boards, created and implemented in the GameLogic class"""
    def__init__(self):
        self.board=[['']*8 for_in range(8)]