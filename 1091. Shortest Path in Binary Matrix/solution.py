Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.

class Solution:

    def is_clear(self,cell,grid):
        return grid[cell[0]][cell[1]] == 0

    def get_neighbours(self,cell,grid):
        (i, j) = cell
        return (
            (i + a, j + b)
            for a in (-1, 0, 1)
            for b in (-1, 0, 1)
            if a != 0 or b != 0
            if 0 <= i + a < len(grid)
            if 0 <= j + b < len(grid)
            if self.is_clear((i + a, j + b),grid)
        )
    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        start = (0, 0)
        goal = (N - 1, N - 1)

        queue = deque()
        if self.is_clear(start,grid):
            queue.append(start)
        visited = set()
        path_len = {start: 1}

        while queue:
            cell = queue.popleft()
            if cell in visited:
                continue
            if cell == goal:
                return path_len[cell]
            visited.add(cell)
            for neighbour in self.get_neighbours(cell,grid):
                if neighbour not in path_len:
                    path_len[neighbour] = path_len[cell] + 1
                queue.append(neighbour)

        return -1