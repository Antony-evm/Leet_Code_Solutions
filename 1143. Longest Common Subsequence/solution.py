# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = map(len, (text1, text2))
        if m < n:
            tex1, tex2 = text2, text1
        dp = [0] * (n + 1)
        for c in text1:
            prevRow, prevRowPrevCol = 0, 0
            for j, d in enumerate(text2):
                prevRow, prevRowPrevCol = dp[j + 1], prevRow
                dp[j + 1] = prevRowPrevCol + 1 if c == d else max(dp[j], prevRow)
        return dp[-1]
        
        

