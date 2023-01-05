from enum import Enum


class Position(Enum):
    TOP_LEFT = 1
    TOP_MIDDLE = 2
    TOP_RIGHT = 3
    MIDDLE_LEFT = 4
    MIDDLE_MIDDLE = 5
    MIDDLE_RIGHT = 6
    BOTTOM_LEFT = 7
    BOTTOM_MIDDDLE = 8
    BOTTOM_RIGHT = 9


class Players(Enum):
    X = 0
    O = 1

    
class Tictactoe:
    def __init__(self) -> None:
       self.current_player = Players.X

    def get_current_player(self):
        return self.current_player

    def change_player(self):
        if self.current_player == Players.X:
            self.current_player = Players.O
            return
        self.current_player = Players.X

    def play(self, position):
        self.change_player()
        return self.current_player

    def get_winner(self):
        return Players.X