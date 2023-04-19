# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index,t_index,t_len,s_len = 0,0,len(t),len(s)

        while t_index<t_len and s_index<s_len:
            if t.find(s[s_index])<0:
                return False
            elif t[t_index] == s[s_index]:
                s_index+=1
            t_index+=1            
        return s_index == s_len
