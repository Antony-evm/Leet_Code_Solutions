# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.
# 1 <= nums.length <= 200
# -109 <= nums[i] <= 109
# -109 <= target <= 109

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        actual_start,covered,res = [],[],[]
        length = len(nums)
        for first_ptr in range(len(nums)):
            first_start = nums[first_ptr]
            if first_start in actual_start:
                continue
            actual_start.append(first_start)
            covered = []
            for index in range(first_ptr+1,len(nums)):
                start = nums[index]
                if start in covered:
                    continue
                covered.append(start)
                left,right = index+1,len(nums)-1
                while left<right:
                    sum4 = nums[left]+nums[right]+start+first_start-target
                    if sum4<0:
                        left+=1
                    elif sum4>0:
                        right-=1
                    else:
                        out = sorted([first_start,start,nums[left],nums[right]])
                        res.append(out)
                        left+=1
                        right-=1
                        while nums[left]==nums[left-1] and left<right:
                            left+=1

        return res