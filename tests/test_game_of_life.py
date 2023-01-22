import pytest
from katas.game_of_life import Game, Cell, CellState


def test_single_cell_dies():

    board = [CellState.ALIVE]
    game = Game(board)

    game.play()

    assert game.next_generation() == [CellState.DEAD]


def test_cell_with_two_neighbours_lives():

    board = [CellState.ALIVE, CellState.ALIVE, CellState.ALIVE]
    game = Game(board)

    game.play()

    assert game.next_generation() == [CellState.DEAD, CellState.ALIVE, CellState.DEAD]
