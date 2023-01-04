import pytest
from katas.tictactoe import Tictactoe, Players

@pytest.fixture
def tictactoe():
    return Tictactoe()


def test_x_goes_first(tictactoe):

    current_player = tictactoe.get_current_player()

    assert current_player == Players.X


def test_o_goes_second(tictactoe):
    
    tictactoe.play()
    current_player = tictactoe.get_current_player()

    assert current_player == Players.O


def test_players_alternate(tictactoe):
    
    tictactoe.play()
    tictactoe.play()
    current_player = tictactoe.get_current_player()

    assert current_player == Players.X