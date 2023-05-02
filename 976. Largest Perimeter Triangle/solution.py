# Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        def perimeter(a, b, c):
            return a + b + c

        def is_valid(a, b, c):
            return a + b > c and a + c > b and b + c > a

        nums.sort()
        for i in range(len(nums) - 1, 1, -1):
            if is_valid(nums[i], nums[i - 1], nums[i - 2]):
                return perimeter(nums[i], nums[i - 1], nums[i - 2])
        return 0
