
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
            total = temp_counter = 0

            for idx in range(1,len(diffs)):
                if diffs[idx-1]==diffs[idx]:
                    counter+=1
                if diffs[idx-1]!=diffs[idx] or idx==len(diffs)-1:
                    temp_counter = counter
                    counter = 1
                    if temp_counter>=2:
                        total+=sum([i for i in range(1,temp_counter)])
                

            return total

