# Given an integer array nums that may contain duplicates, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)+1):
            for combo in list(itertools.combinations(nums,i)):
                combo = sorted(list(combo))
                if combo not in res:
                    res+=[combo]
        return res

        