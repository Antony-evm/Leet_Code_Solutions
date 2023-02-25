# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, 
# and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        covered,res = [],[]
        length = len(nums)
        for index in range(length):
            start = nums[index]
            if start in covered:
                continue
            covered.append(start)
            left,right = index+1,len(nums)-1
            while left<right:
                sum3 = nums[left]+nums[right]+start
                if sum3<0:
                    left+=1
                elif sum3>0:
                    right-=1
                else:
                    out = sorted([start,nums[left],nums[right]])
                    res.append(out)
                    left+=1
                    right-=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1

        return res