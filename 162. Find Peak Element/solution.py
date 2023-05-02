# A peak element is an element that is strictly greater than its neighbors.

# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

# You must write an algorithm that runs in O(log n) time.


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        l, r = 0, len(nums)
        while l < r - 1:
            if ((l == 0) or (l != 0 and nums[l] > nums[l - 1])) and nums[l] > nums[l + 1]:
                return l
            else:
                if nums[l] <= nums[l + 1]:
                    l += 1
                else:
                    l += 2

        return l
