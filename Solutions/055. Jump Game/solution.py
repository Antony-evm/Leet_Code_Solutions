# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_position = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if (i + nums[i]) >= last_position:
                last_position = i
        return last_position == 0


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        @lru_cache(None)
        def dp(i):
            if i == n - 1:
                return True

            for j in range(i + 1, min(i + nums[i], n - 1) + 1):
                if dp(j):
                    return True
            return False

        return dp(0)
