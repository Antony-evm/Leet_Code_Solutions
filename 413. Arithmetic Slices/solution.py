
# An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

# For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
# Given an integer array nums, return the number of arithmetic subarrays of nums.

# A subarray is a contiguous subsequence of the array.

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums)<3:
            return 0
        else:
            diffs = list(starmap(operator.sub,zip(nums[1:],nums)))
            counter = 1
            total = 0

            for idx in range(1,len(diffs)):
                if diffs[idx-1]==diffs[idx] and idx<len(diffs)-1:
                    counter+=1
                elif diffs[idx-1]!=diffs[idx]:
                    if counter>=2:
                        total+=counter*(counter-1)//2
                    counter = 1
                else:
                    counter+=1
                    if counter>=2:
                        total+=counter*(counter-1)//2
                
            return total

