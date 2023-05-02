# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

# You can either start from the step with index 0, or the step with index 1.

# Return the minimum cost to reach the top of the floor.


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cur = 0
        dp0, dp1 = cost[0], cost[1]

        for i in range(2, len(cost)):
            cur = cost[i] + min(dp0, dp1)
            dp0 = dp1
            dp1 = cur
        return min(dp0, dp1)
