from dataclasses import dataclass
from enum import Enum


class CellState(Enum):
    DEAD = 0
    ALIVE = 1


@dataclass
class Cell:
    def __init__(self, cell_state, position) -> None:
        self.cell_state = cell_state
        self.position = position


class Game:
    def __init__(self, board) -> None:
        self.board = board

    def play(self):
        if len(self.board) > 2:
            return (
                [Cell(CellState.DEAD, self.board[0].position)]
                + [Cell(CellState.ALIVE, cell.position) for cell in self.board[1:-1]]
                + [Cell(CellState.DEAD, self.board[-1].position)]
            )
        return [Cell(CellState.DEAD, cell.position) for cell in self.board]
