# Given an integer array nums, return the length of the longest strictly increasing


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = 1
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    ans = max(ans, dp[i])


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = 1
        temp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > temp[-1]:
                temp.append(nums[i])
                lis += 1
            else:
                temp[bisect_left(temp, nums[i])] = nums[i]
        return lis
