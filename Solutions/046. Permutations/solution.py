# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        import itertools

        return list(itertools.permutations(nums))
