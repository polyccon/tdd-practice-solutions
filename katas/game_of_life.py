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
        one_dead_cell = [CellState.DEAD]
        if len(self.board) == 1:
            return one_dead_cell
        alive_cells = [CellState.ALIVE for cell in enumerate(self.board[0:-2])]
        return one_dead_cell + alive_cells + one_dead_cell

