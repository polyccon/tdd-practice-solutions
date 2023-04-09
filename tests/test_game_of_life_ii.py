import pytest
from katas.game_of_life_ii import Game, CellState


def test_single_cell_dies():
    board = [CellState.ALIVE]
    game = Game(board)

    next_generation = game.play()

    assert next_generation == [CellState.DEAD]


def test_cell_with_one_neighbour_dies():
    board = [CellState.ALIVE, CellState.ALIVE]
    game = Game(board)

    next_generation = game.play()

    assert next_generation == [CellState.DEAD, CellState.DEAD]
