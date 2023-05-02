# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        import itertools

        return list(set(itertools.permutations(nums)))
