import pytest
from katas.game_of_life import Game, CellState


def test_single_cell_dies():

    board = [CellState.ALIVE]
    game = Game(board)

    game.play()

    assert game.next_generation() == [CellState.DEAD]