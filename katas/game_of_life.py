from enum import Enum


class CellState(Enum):
    ALIVE = 1
    DEAD = 0


class Position:
    def __init__(self, position) -> None:
        x, y = position
        self.x = x
        self.y = y

    def __repr__(self):
        return str(self.x) + "-" + str(self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def _is_neighbour(self, other):
        return self.x - other.x in [-1, 1] or self.y - other.y in [-1, 1]


class Board:
    def __init__(self, cells):
        self.cells = cells

    def get_alive_neighbours_count(self, cell):
        alive_neighbours = 0
        for _cell in self.cells:
            if _cell.is_neighbour(cell) and _cell.is_alive():
                alive_neighbours += 1
        return alive_neighbours

    def evolve_cell_state(self):
        evolved_cells = []
        for cell in self.cells:
            alive_neighbours = self.get_alive_neighbours_count(cell)
            evolved_cells.append(cell.evolve(alive_neighbours))
        return evolved_cells


class Cell:
    def __init__(self, cell_state, position) -> None:
        self.cell_state = cell_state
        self.position = position

    def __eq__(self, other):
        return (
           self.cell_state == other.cell_state
           and self.position == other.position
        )

    def is_alive(self):
        return self.cell_state == CellState.ALIVE

    def is_neighbour(self, other):
        return Position(self.position)._is_neighbour(Position(other.position))

    def get_cell_state(self):
        return self.cell_state

    def evolve(self, alive_neighbours_count):
        if alive_neighbours_count > 1:
            return Cell(CellState.ALIVE, self.position)
        return Cell(CellState.DEAD, self.position)


class Game:
    def __init__(self, board) -> None:
        self.board = Board(board)

    def play(self):
        return self.board.evolve_cell_state()

    def next_generation(self):
        return self.play()
