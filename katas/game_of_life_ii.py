from enum import Enum


class CellState(Enum):
    DEAD = 0
    ALIVE = 1


class Game:
    def __init__(self, board) -> None:
        self.board = board

    def play(self):
        return [CellState.DEAD for cell in self.board]
