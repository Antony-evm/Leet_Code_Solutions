# Given an integer array nums, find the subarray with the largest sum, and return its sum.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        from itertools import accumulate
        return max(accumulate(nums, lambda x, y: x+y if x > 0 else y))



