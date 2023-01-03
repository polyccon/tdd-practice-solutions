from enum import Enum


class Players(Enum):
    X = 0

    
class Tictactoe:
    def get_current_player(self):
        return Players.X