# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_left(nums, target + 1)
        return left if left != right else -1
