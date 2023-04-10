from enum import Enum


class CellState(Enum):
    DEAD = 0
    ALIVE = 1


class Position:
    POSITION_DELTA = [-1, 1]

    def __init__(self, coordinates) -> None:
        (x, y) = coordinates
        self.x = x
        self.y = y

    def get_neighbour_positions(self):
        return [(self.x + delta, self.y) for delta in self.POSITION_DELTA]

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Cell:
    def __init__(self, cell_state, coordinates) -> None:
        self.cell_state = cell_state
        self.position = Position(coordinates)

    def get_neighbour_positions(self):
        return self.position.get_neighbour_positions()

    def __eq__(self, other):
        return self.cell_state == other.cell_state and self.position == other.position

    def evolve(self, number_of_neighbours):
        self.cell_state = (
            CellState.DEAD if number_of_neighbours < 2 else CellState.ALIVE
        )


class Game:
    def __init__(self, board) -> None:
        self.board = board

    def calculate_number_of_neighbours(self, cell):
        count = 0
        neighbour_positions = cell.get_neighbour_positions()
        for neighbour_position in neighbour_positions:
            if neighbour_position in [
                (cell.position.x, cell.position.y) for cell in self.board
            ]:
                count += 1
        return count

    def play(self):
        for cell in self.board:
            number_of_neighbours = self.calculate_number_of_neighbours(cell)
            cell.evolve(number_of_neighbours)
        return self.board
