import pytest
from katas.game_of_life import Game, Cell, CellState


def test_single_cell_dies():

    board = [Cell(CellState.ALIVE, (0, 0))]
    expected_output = [Cell(CellState.DEAD, (0, 0))]
    game = Game(board)

    output = game.next_generation()

    assert output == expected_output


def test_two_cells_die():

    board = [
        Cell(CellState.ALIVE, (0, 0)),
        Cell(CellState.ALIVE, (0, 1))
    ]
    expected_output = [
        Cell(CellState.DEAD, (0, 0)),
        Cell(CellState.DEAD, (0, 1))
    ]
    game = Game(board)

    output = game.next_generation()

    assert output == expected_output


def test_cell_with_two_neighbours_lives():

    board = [
        Cell(CellState.ALIVE, (0, 0)),
        Cell(CellState.ALIVE, (0, 1)),
        Cell(CellState.ALIVE, (0, 2))
    ]
    expected_output = [
        Cell(CellState.DEAD, (0, 0)),
        Cell(CellState.ALIVE, (0, 1)),
        Cell(CellState.DEAD, (0, 2))
    ]
    game = Game(board)

    output = game.next_generation()

    assert output == expected_output


def test_four_cells_in_a_row_middle_ones_live():

    board = [
        Cell(CellState.ALIVE, (0, 0)),
        Cell(CellState.ALIVE, (0, 1)),
        Cell(CellState.ALIVE, (0, 2)),
        Cell(CellState.ALIVE, (0, 3))
    ]
    expected_output = [
        Cell(CellState.DEAD, (0, 0)),
        Cell(CellState.ALIVE, (0, 1)),
        Cell(CellState.ALIVE, (0, 2)),
        Cell(CellState.DEAD, (0, 3))
    ]
    game = Game(board)

    output = game.next_generation()

    assert output == expected_output


def test_four_cells_in_a_row_one_dead_middle_ones_live():

    board = [
        Cell(CellState.ALIVE, (0, 0)),
        Cell(CellState.ALIVE, (0, 1)),
        Cell(CellState.ALIVE, (0, 2)),
        Cell(CellState.DEAD, (0, 3))
    ]
    expected_output = [
        Cell(CellState.DEAD, (0, 0)),
        Cell(CellState.ALIVE, (0, 1)),
        Cell(CellState.DEAD, (0, 2)),
        Cell(CellState.DEAD, (0, 3))
    ]
    game = Game(board)

    output = game.next_generation()

    assert output == expected_output


def test_four_cells_in_a_square_all_live():

    board = [
        Cell(CellState.ALIVE, (0, 0)),
        Cell(CellState.ALIVE, (0, 1)),
        Cell(CellState.ALIVE, (1, 0)),
        Cell(CellState.ALIVE, (1, 1))
    ]
    expected_output = [
        Cell(CellState.ALIVE, (0, 0)),
        Cell(CellState.ALIVE, (0, 1)),
        Cell(CellState.ALIVE, (1, 0)),
        Cell(CellState.ALIVE, (1, 1))
    ]
    game = Game(board)

    output = game.next_generation()

    assert output == expected_output