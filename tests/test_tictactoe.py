import pytest
from katas.tictactoe import Tictactoe


def test_x_goes_first():
    tictactoe = Tictactoe()

    current_player = tictactoe.get_current_player()

    assert current_player == "X"