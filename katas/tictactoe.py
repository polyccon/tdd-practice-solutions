from enum import Enum


class Tiles(Enum):
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
    X = "X"
    O = "O"
    DRAW = "DRAW"


class Board:
    def __init__(self) -> None:
        self.tiles = {}

    def mark_at(self, position, current_player):
        self.tiles[position] = current_player

    def get_winner(self):
        if self.tiles.get(Tiles.TOP_LEFT) == self.tiles.get(
            Tiles.TOP_MIDDLE
        ) and self.tiles.get(Tiles.TOP_MIDDLE) == self.tiles.get(Tiles.TOP_RIGHT):
            return self.tiles.get(Tiles.TOP_LEFT)


class Tictactoe:
    def __init__(self) -> None:
       self.current_player = Players.X
       self.board = Board()

    def get_current_player(self):
        return self.current_player

    def change_player(self):
        if self.current_player == Players.X:
            self.current_player = Players.O
            return
        self.current_player = Players.X

    def play(self, position):
        self.board.mark_at(position, self.current_player)
        self.change_player()
        return self.current_player

    def get_winner(self):
        return self.board.get_winner()