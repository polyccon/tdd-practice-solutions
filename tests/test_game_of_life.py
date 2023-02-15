import pytest
from katas.game_of_life import Game, Cell, CellState, Position


def test_single_cell_dies():

    board = [Cell(CellState.ALIVE, Position(0, 0))]
    expected_output = [Cell(CellState.DEAD, Position(0, 0))]
    game = Game(board)

    output = game.next_generation()

    assert output == expected_output


def test_two_cells_die():

    board = [
        Cell(CellState.ALIVE, Position(0, 0)),
        Cell(CellState.ALIVE, Position(0, 1))
    ]
    expected_output = [
        Cell(CellState.DEAD, Position(0, 0)),
        Cell(CellState.DEAD, Position(0, 1))
    ]
    game = Game(board)

    output = game.next_generation()

    assert output == expected_output


def test_cell_with_two_neighbours_lives():

    board = [
        Cell(CellState.ALIVE, Position(0, 0)),
        Cell(CellState.ALIVE, Position(0, 1)),
        Cell(CellState.ALIVE, Position(0, 2))
    ]
    expected_output = [
        Cell(CellState.DEAD, Position(0, 0)),
        Cell(CellState.ALIVE, Position(0, 1)),
        Cell(CellState.DEAD, Position(0, 2))
    ]
    game = Game(board)

    output = game.next_generation()

    assert output == expected_output


def test_four_cells_in_a_row_middle_ones_live():

    board = [
        Cell(CellState.ALIVE, Position(0, 0)),
        Cell(CellState.ALIVE, Position(0, 1)),
        Cell(CellState.ALIVE, Position(0, 2)),
        Cell(CellState.ALIVE, Position(0, 3))
    ]
    expected_output = [
        Cell(CellState.DEAD, Position(0, 0)),
        Cell(CellState.ALIVE, Position(0, 1)),
        Cell(CellState.ALIVE, Position(0, 2)),
        Cell(CellState.DEAD, Position(0, 3))
    ]
    game = Game(board)

    output = game.next_generation()

    assert output == expected_output