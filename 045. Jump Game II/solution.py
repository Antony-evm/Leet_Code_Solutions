# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].


class Solution:
    def jump(self, A):
        last_max_reach, current_max_reach = 0, 0
        njump, i = 0, 0
        while current_max_reach < len(A) - 1:
            while i <= last_max_reach:
                current_max_reach = max(i + A[i], current_max_reach)
                i += 1
            if last_max_reach == current_max_reach:
                return -1
            last_max_reach = current_max_reach
            njump += 1
        return njump
