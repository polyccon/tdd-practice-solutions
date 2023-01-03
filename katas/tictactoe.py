from enum import Enum


class Players(Enum):
    X = 0
    O = 1

    
class Tictactoe:
    def __init__(self) -> None:
       self.current_player = Players.X

    def get_current_player(self):
        return self.current_player

    def play(self):
        self.current_player = Players.O