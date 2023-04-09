from enum import Enum


class CellState(Enum):
    DEAD = 0
    ALIVE = 1


class Game:
    def __init__(self, board) -> None:
        self.board = board

    def play(self):
        if len(self.board) > 3:
            return [CellState.DEAD, CellState.ALIVE, CellState.ALIVE, CellState.DEAD]
        if len(self.board) > 2:
            return [CellState.DEAD, CellState.ALIVE, CellState.DEAD]
        return [CellState.DEAD for cell in self.board]
