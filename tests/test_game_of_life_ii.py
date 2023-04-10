import pytest
from katas.game_of_life_ii import Game, Cell, CellState


def test_single_cell_dies():
    board = [Cell(CellState.ALIVE, (0, 0))]
    game = Game(board)

    game.play()

    assert board == [Cell(CellState.DEAD, (0, 0))]


def test_cell_with_one_neighbour_in_a_row_dies():
    board = [Cell(CellState.ALIVE, (0, 0)), Cell(CellState.ALIVE, (1, 0))]
    game = Game(board)

    game.play()

    assert board == [
        Cell(CellState.DEAD, (0, 0)),
        Cell(CellState.DEAD, (1, 0)),
    ]


def test_cell_with_two_neighbours_in_a_row_lives():
    board = [
        Cell(CellState.ALIVE, (0, 0)),
        Cell(CellState.ALIVE, (1, 0)),
        Cell(CellState.ALIVE, (2, 0)),
    ]
    game = Game(board)

    game.play()

    assert board == [
        Cell(CellState.DEAD, (0, 0)),
        Cell(CellState.ALIVE, (1, 0)),
        Cell(CellState.DEAD, (2, 0)),
    ]


def test_cell_with_three_neighbours_in_a_row_lives():
    board = [
        Cell(CellState.ALIVE, (0, 0)),
        Cell(CellState.ALIVE, (1, 0)),
        Cell(CellState.ALIVE, (2, 0)),
        Cell(CellState.ALIVE, (3, 0)),
    ]
    game = Game(board)

    game.play()

    assert board == [
        Cell(CellState.DEAD, (0, 0)),
        Cell(CellState.ALIVE, (1, 0)),
        Cell(CellState.ALIVE, (2, 0)),
        Cell(CellState.DEAD, (3, 0)),
    ]
