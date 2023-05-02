# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dq = deque()
        seen = {}
        islands = 0
        cols = len(grid[0])
        rows = len(grid)
        for row in range(rows):
            for col in range(cols):
                if seen.get((row, col), -1) == 0:
                    continue
                if grid[row][col] == "0":
                    seen[(row, col)] = 0
                else:
                    if seen.get((row, col), -1) == -1:
                        dq.append([row, col])
                        seen[(row, col)] = 0
                        islands += 1
                        while dq:
                            x, y = dq.popleft()
                            if x > 0:
                                if grid[x - 1][y] == "1" and seen.get((x - 1, y), -1) == -1:
                                    dq.append([x - 1, y])
                                seen[(x - 1, y)] = 0

                            if x < rows - 1:
                                if grid[x + 1][y] == "1" and seen.get((x + 1, y), -1) == -1:
                                    dq.append([x + 1, y])
                                seen[(x + 1, y)] = 0

                            if y > 0:
                                if grid[x][y - 1] == "1" and seen.get((x, y - 1), -1) == -1:
                                    dq.append([x, y - 1])
                                seen[(x, y - 1)] = 0

                            if y < cols - 1:
                                if grid[x][y + 1] == "1" and seen.get((x, y + 1), -1) == -1:
                                    dq.append([x, y + 1])
                                seen[(x, y + 1)] = 0
        return islands
