# Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

# In one step, you can delete exactly one character in either string.

class Solution:
    def minDistance(self, text1: str, text2: str) -> int:
        m, n = map(len, (text1, text2))
        if m < n:
            tex1, tex2 = text2, text1
        dp = [0] * (n + 1)
        for c in text1:
            prevRow, prevRowPrevCol = 0, 0
            for j, d in enumerate(text2):
                prevRow, prevRowPrevCol = dp[j + 1], prevRow
                dp[j + 1] = prevRowPrevCol + 1 if c == d else max(dp[j], prevRow)
        return len(text2)+len(text1)-dp[-1]*2