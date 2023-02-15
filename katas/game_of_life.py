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

    def _is_neighbour(self, other):
        return self.x - other.x in [ -1, 1] or self.y - other.y in [ -1, 1]


class Board:
    def __init__(self, cells):
        self.cells = cells

    def get_alive_neighbours_count(self, cell):
        alive_neighbours = 0
        for _cell in self.cells:
            if cell.is_neighbour(_cell):
                alive_neighbours += 1
        return alive_neighbours

    def evolve_cell_state(self):
        evolved_cells = []
        for cell in cells:
            alive_neighbours = self.get_alive_neighbours_count(cell)
            cell.evolve_cell_state(alive_neighbours)
            evolved_cells.append(cell)
        return evolved_cells


class Cell:
    def __init__(self, cell_state, position):
        self.cell_state = cell_state
        self.position = position

    def __eq__(self, other):
        return (
           self.cell_state == other.cell_state
           and self.position == other.position
            )

    def is_neighbour(self, other):
        return self.position._is_neighbour(other.position)

    def evolve_cell_state(self, alive_neighbours_count):
        if alive_neighbours_count > 1:
            self.cell_state = CellState.ALIVE
            return
        self.cell_state = CellState.DEAD


class Game():
    def __init__(self, board) -> None:
        self.board = Board(board)


    def play(self):
        for cell in self.board.cells:
            alive_neighbours_count = self.board.get_alive_neighbours_count(cell)
            cell.evolve_cell_state(alive_neighbours_count)
        return self.board.cells

    def next_generation(self):
        return self.play()