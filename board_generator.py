import numpy as np


class BoardGenerator:
    def __init__(self, rows, cols, level):
        self.raw_board = self.create_board(rows, cols, level)
        self.arm_board()
        self.board = self.add_coords()

    def create_board(self, rows, cols, level):
        return np.random.binomial(n=1, p=level, size=[rows, cols])

    def arm_board(self):
        for row, col in np.ndindex(self.raw_board.shape):
            if self.raw_board[row, col] == 1:
                proxy_cels = self.raw_board[max(row - 1, 0):row + 2,
                                            max(col - 1, 0):col + 2]
                bomb_count = np.count_nonzero(proxy_cels == 0)
                self.raw_board[row, col] = bomb_count if bomb_count > 0 else 9

    def add_coords(self):
        board = list(self.raw_board)
        new_board = []
        for x, row in enumerate(board):
            new_row = [{'id': [x + 1, y + 1],
                        'value': int(board[x][y])} for y, _ in enumerate(row)]
            new_board.append(new_row)

        return new_board
