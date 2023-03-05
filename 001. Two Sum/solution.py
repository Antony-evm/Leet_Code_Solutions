Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        import numpy as np
        left,right = 0,len(nums)-1
        sorted_nums = np.argsort(np.array(nums))
        while left<right:
            res = nums[sorted_nums[left]] + nums[sorted_nums[right]] - target
            if res<0:
                left+=1
            elif res>0:
                right-=1
            else:
                return [sorted_nums[left],sorted_nums[right]]
