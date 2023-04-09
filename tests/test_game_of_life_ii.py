import pytest
from katas.game_of_life_ii import Game, Cell, CellState


def test_single_cell_dies():
    board = [Cell(CellState.ALIVE, 0)]
    game = Game(board)

    next_generation = game.play()

    assert next_generation == [Cell(CellState.DEAD, 0)]


def test_cell_with_one_neighbour_dies():
    board = [Cell(CellState.ALIVE, 0), Cell(CellState.ALIVE, 1)]
    game = Game(board)

    next_generation = game.play()

    assert next_generation == [Cell(CellState.DEAD, 0), Cell(CellState.DEAD, 1)]


def test_cell_with_two_neighbours_lives():
    board = [
        Cell(CellState.ALIVE, 0),
        Cell(CellState.ALIVE, 1),
        Cell(CellState.ALIVE, 2),
    ]
    game = Game(board)

    next_generation = game.play()

    assert next_generation == [
        Cell(CellState.DEAD, 0),
        Cell(CellState.ALIVE, 1),
        Cell(CellState.DEAD, 2),
    ]


def test_cell_with_three_neighbours_lives():
    board = [
        Cell(CellState.ALIVE, 0),
        Cell(CellState.ALIVE, 1),
        Cell(CellState.ALIVE, 2),
        Cell(CellState.ALIVE, 3),
    ]
    game = Game(board)

    next_generation = game.play()

    assert next_generation == [
        Cell(CellState.DEAD, 0),
        Cell(CellState.ALIVE, 1),
        Cell(CellState.ALIVE, 2),
        Cell(CellState.DEAD, 3),
    ]
