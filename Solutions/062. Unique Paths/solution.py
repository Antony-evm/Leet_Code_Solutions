# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return factorial(m + n - 2) // (factorial(n - 1) * factorial(m - 1))


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def factorial(m):
            return list(accumulate([i for i in range(1, m + 1)], lambda x, y: x * y))[-1]

        return factorial(m + n - 2) // (factorial(n - 1) * factorial(m - 1)) if m > 1 and n > 1 else 1


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.paths(m, n)

    @lru_cache(None)
    def paths(self, m, n):
        if m < 0 or n < 0:
            return 0
        if m == 1 and n == 1:
            return 1
        return self.paths(m - 1, n) + self.paths(m, n - 1)
