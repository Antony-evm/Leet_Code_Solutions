# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

import itertools


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            nrow = [i for i in board[row] if i.isnumeric()]
            if len(set(nrow)) != len(nrow):
                return False

        for col in range(9):
            ncol = []
            for row in range(9):
                element = board[row][col]
                if element.isnumeric():
                    ncol += [element]
            if len(set(ncol)) != len(ncol):
                return False

        step = 3
        for row in range(0, 9, step):
            for col in range(0, 9, step):
                triangle = [
                    i
                    for i in itertools.chain(*[j[col : col + step] for j in board[row : row + step]])
                    if i.isnumeric()
                ]
                if len(triangle) != len(set(triangle)):
                    return False
        return True
