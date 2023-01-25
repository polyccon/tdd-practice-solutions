from enum import Enum


class CellState(Enum):
    ALIVE = 1
    DEAD = 0


class Position:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        
    def __repr__(self):
        return str(self.x) + "-" + str(self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Cell:
    def __init__(self, cell_state, position):
        self.cell_state = cell_state
        self.position = position

    def __eq__(self, other):
        return (
           self.cell_state == other.cell_state
           and self.position == other.position
            )


class Game():
    def __init__(self, board) -> None:
        self.board = board

    def play(self):
        pass  

    def next_generation(self):
        output = []
        for index, cell in enumerate(self.board):
            cell_state = CellState.DEAD if index in [0, len(self.board)-1] else CellState.ALIVE
            output.append(Cell(cell_state, Position(cell.position.x, cell.position.y)))
        return output
