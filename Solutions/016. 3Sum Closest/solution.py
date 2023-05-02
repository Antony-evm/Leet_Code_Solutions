# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.
# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        covered = []
        nums.sort()
        length = len(nums)
        res = 10000 * 3
        for index in range(length):
            start = nums[index]
            if start in covered:
                continue
            covered.append(start)
            left, right = index + 1, length - 1
            while left < right:
                sum3 = start + nums[left] + nums[right] - target

                res = res if abs(sum3) > abs(res) else sum3
                if sum3 < 0:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif sum3 > 0:
                    right -= 1
                    while left < right and nums[right + 1] == nums[right]:
                        right -= 1
                else:
                    return res + target

        return res + target
