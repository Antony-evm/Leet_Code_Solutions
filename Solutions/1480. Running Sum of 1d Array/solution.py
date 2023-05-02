# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(accumulate(nums))


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        rs = 0
        for i in range(len(nums)):
            rs += nums[i]
            nums[i] = rs

        return nums
