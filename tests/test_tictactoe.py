import pytest
from katas.tictactoe import Tictactoe, Players, Tiles

@pytest.fixture
def tictactoe():
    return Tictactoe()


def test_x_goes_first(tictactoe):

    current_player = tictactoe.get_current_player()

    assert current_player == Players.X


def test_o_goes_second(tictactoe):
    
    tictactoe.play(Tiles.MIDDLE_MIDDLE)
    current_player = tictactoe.get_current_player()

    assert current_player == Players.O


def test_players_alternate(tictactoe):
    
    tictactoe.play(Tiles.TOP_LEFT)
    tictactoe.play(Tiles.MIDDLE_MIDDLE)
    current_player = tictactoe.get_current_player()

    assert current_player == Players.X


def test_3_x_in_top_row_gives_x_as_winner(tictactoe):

    tictactoe.play(Tiles.TOP_LEFT)
    tictactoe.play(Tiles.MIDDLE_MIDDLE)
    tictactoe.play(Tiles.TOP_MIDDLE)
    tictactoe.play(Tiles.BOTTOM_RIGHT)
    tictactoe.play(Tiles.TOP_RIGHT)

    winner = tictactoe.get_winner()

    assert winner == Players.X


def  test_3_o_in_top_row_gives_o_as_winner(tictactoe):

    tictactoe.play(Tiles.BOTTOM_RIGHT)
    tictactoe.play(Tiles.TOP_RIGHT)
    tictactoe.play(Tiles.BOTTOM_LEFT)
    tictactoe.play(Tiles.TOP_LEFT)
    tictactoe.play(Tiles.MIDDLE_MIDDLE)
    tictactoe.play(Tiles.TOP_MIDDLE)
    
    winner = tictactoe.get_winner()

    assert winner == Players.O