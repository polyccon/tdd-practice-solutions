from enum import Enum


class CellState(Enum):
    DEAD = 0
    ALIVE = 1


POSITION_DELTA = [-1, 1]


class Cell:
    def __init__(self, cell_state, position) -> None:
        self.cell_state = cell_state
        self.position = position

    def get_neighbour_positions(self):
        return [
            (self.position[0] + delta, self.position[1]) for delta in POSITION_DELTA
        ]

    def __eq__(self, other):
        return self.cell_state == other.cell_state and self.position == other.position

    def evolve(self, number_of_neighbours):
        return CellState.DEAD if number_of_neighbours < 2 else CellState.ALIVE


class Game:
    def __init__(self, board) -> None:
        self.board = board

    def calculate_number_of_neighbours(self, cell):
        count = 0
        neighbour_positions = cell.get_neighbour_positions()
        for neighbour_position in neighbour_positions:
            if neighbour_position in [cell.position for cell in self.board]:
                count += 1
        return count

    def play(self):
        next_generation = []
        for cell in self.board:
            number_of_neighbours = self.calculate_number_of_neighbours(cell)
            cell_state = cell.evolve(number_of_neighbours)
            next_generation.append(Cell(cell_state, cell.position))
        return next_generation
