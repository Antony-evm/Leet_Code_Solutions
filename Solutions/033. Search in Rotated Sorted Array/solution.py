# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        mid = 0
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        nleft = nums[:r]
        nright = nums[r:]
        if target > max(nright):
            l = bisect.bisect_left(nleft, target)
            r = bisect.bisect_left(nleft, target + 1)
            return -1 if l == r else l
        elif target <= max(nright):
            l = bisect.bisect_left(nright, target)
            r = bisect.bisect_left(nright, target + 1)
            return -1 if l == r else l + len(nleft)
