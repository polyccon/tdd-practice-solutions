from enum import Enum


class CellState(Enum):
    ALIVE = 1
    DEAD = 0


class Game():
    def __init__(self, board) -> None:
        self.board = board

    def play(self):
        pass  

    def next_generation(self):
        return [CellState.DEAD]

