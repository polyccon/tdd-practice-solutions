from enum import Enum


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
        else:
            self.current_player = Players.X

    def play(self):
        self.change_player()
        return self.current_player