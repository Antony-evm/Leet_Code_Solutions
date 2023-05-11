# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        length = len(nums)
        if length == 0:
            return 0
        return (
            nums[length // 2]
            if len(nums) % 2 == 1
            else (nums[length // 2] + nums[length // 2 - 1]) / 2
        )
