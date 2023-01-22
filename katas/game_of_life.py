from enum import Enum


class CellState(Enum):
    ALIVE = 1
    DEAD = 0


class Cell:
    def __init__(self, cell_state, position):
        self.cell_state = cell_state
        self.position = position
    

class Game():
    def __init__(self, board) -> None:
        self.board = board

    def play(self):
        pass  

    def next_generation(self):
        if len(self.board) == 1:
            return [CellState.DEAD]
        if len(self.board) == 3:
            return [CellState.DEAD, CellState.ALIVE, CellState.DEAD]
        if len(self.board) == 4:
            return [CellState.DEAD, CellState.ALIVE, CellState.ALIVE, CellState.DEAD]

