# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        not_turn = []
        visited = []
        potential = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row == 0 or row == len(board) - 1) or (col == 0 or col == len(board[0]) - 1):
                    visited.append((row, col))
                    if board[row][col] == "O":
                        not_turn.append((row, col))

        stack = deque(not_turn)
        while stack:
            cell = stack.popleft()
            for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                potential = (cell[0] + direction[0], cell[1] + direction[1])
                if potential not in visited and 0 <= potential[0] < len(board) and 0 <= potential[1] < len(board[0]):
                    visited.append(potential)
                    if board[potential[0]][potential[1]] == "O":
                        not_turn.append(potential)
                        stack.append(potential)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row, col) not in visited and (row, col) not in not_turn:
                    board[row][col] = "X"
