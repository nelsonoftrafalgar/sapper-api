import pytest
from sapper.board_generator import BoardGenerator


@pytest.fixture
def board_generator():
    return BoardGenerator(15, 15, .5)


def test_create_board(board_generator):
    board = board_generator.create_board(5, 5, .4)
    for number in range(0, 2):
        assert number in board
    for number in range(2, 10):
        assert number not in board
    assert board.shape == (5, 5)


def test_arm_board(board_generator):
    board_generator.arm_board()
    for number in range(0, 5):
        assert number in board_generator.raw_board


def test_add_coords(board_generator):
    board = board_generator.add_coords()
    for x, row in enumerate(board):
        for y, _ in enumerate(row):
            item = board[x][y]
            assert item.keys() == {'id', 'value'}
            assert len(item['id']) == 2
            assert item['value'] > -1 and item['value'] < 10
