import pytest
from katas.tictactoe import Tictactoe, Players


def test_x_goes_first():
    tictactoe = Tictactoe()

    current_player = tictactoe.get_current_player()

    assert current_player == Players.X


def test_o_goes_second():
    tictactoe = Tictactoe()
    
    tictactoe.play()
    current_player = tictactoe.get_current_player()

    assert current_player == Players.O


def test_players_alternate():
    tictactoe = Tictactoe()
    
    tictactoe.play()
    tictactoe.play()
    current_player = tictactoe.get_current_player()

    assert current_player == Players.X