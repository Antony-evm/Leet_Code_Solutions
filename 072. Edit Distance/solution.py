# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n ,m = len(word1),len(word2)
        @lru_cache(None)
        def rec(i,j):
            if(i==n and j==m): return 0
            elif(i==n):        return m-j
            elif(j==m):        return n-i
            elif(word1[i]==word2[j]):
                 return rec(i+1,j+1)
            else:
                res = 1+ rec(i,j+1) 
                res = min(res,1+ rec(i+1,j))
                res = min( res, 1+ rec(i+1,j+1))
            return res
        return rec(0,0)