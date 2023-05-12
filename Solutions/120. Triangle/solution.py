# Given a triangle array, return the minimum path sum from top to bottom.

# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]

        @cache
        def dp(i: int, j: int) -> int:
            if i == len(triangle):
                return 0
            lower_left = triangle[i][j] + dp(i + 1, j)
            lower_right = triangle[i][j] + dp(i + 1, j + 1)
            return min(lower_left, lower_right)

        return dp(0, 0)
