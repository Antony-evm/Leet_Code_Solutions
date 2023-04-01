# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
 
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        windowStart = 0
        minWindowSize = len(nums)+1
        runningSum = 0
        for windowEnd in range(0,len(nums)):
            runningSum+=nums[windowEnd]
            while runningSum>=target:
                if runningSum >= target:
                    minWindowSize = min(minWindowSize,windowEnd-windowStart+1)
                runningSum -= nums[windowStart]
                windowStart+=1
      
        return minWindowSize if minWindowSize<len(nums)+1 else 0

