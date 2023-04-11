# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

 
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for i in range(n+1)]
        dp[0] = True
        for i in range(1,n+1):
            for w in wordDict:
                if dp[i-len(w)] and s[i-len(w):i]==w:
                    dp[i]=True
        return dp[-1]