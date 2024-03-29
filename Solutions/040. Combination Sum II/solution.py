# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.


class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()

        def dfs(idx, path, cur):
            if cur > target:
                return
            if cur == target:
                res.append(path)
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                dfs(i + 1, path + [candidates[i]], cur + candidates[i])

        dfs(0, [], 0)
        return res
