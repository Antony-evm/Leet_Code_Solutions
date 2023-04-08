# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.


class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(left, right):
            dp, dp1, dp2 = 0, 0, 0
            for i in range(left, right+1):
                dp = max(dp1, dp2 + nums[i])
                dp2 = dp1
                dp1 = dp
            return dp1
        
        n = len(nums)
        if n == 1: return nums[0]
        return max(solve(0, n-2), solve(1, n-1))