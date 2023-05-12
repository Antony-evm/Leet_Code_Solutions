# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def solve(bo):
            find = find_empty(bo)
            if not find:
                return True
            else:
                row, col = find

            for i in range(1,10):
                if valid(bo, i, (row, col)):
                    bo[row][col] = str(i)

                    if solve(bo):
                        return True

                    bo[row][col] = '.'

            return False


        def valid(bo, num, pos):
            for i in range(len(bo[0])):
                if bo[pos[0]][i] == str(num) and pos[1] != str(i):
                    return False

            for i in range(len(bo)):
                if bo[i][pos[1]] == str(num) and pos[0] != str(i):
                    return False

            box_x = int(pos[1]) // 3
            box_y = int(pos[0]) // 3

            for i in range(box_y*3, box_y*3 + 3):
                for j in range(box_x * 3, box_x*3 + 3):
                    if bo[i][j] == str(num) and (i,j) != str(pos):
                        return False

            return True
        def find_empty(bo):
            for i in range(len(bo)):
                for j in range(len(bo[0])):
                    if bo[i][j] == '.':
                        return (i, j)  # row, col

            return None

        solve(board)