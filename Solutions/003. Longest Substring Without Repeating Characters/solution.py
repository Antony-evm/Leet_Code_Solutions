# Given a string s, find the length of the longest substring without repeating characters


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxx = 0
        if len(s) < 2:
            return len(s)
        else:
            for i in range(len(s)):
                for j in range(len(s[i:])):
                    if (len(s[i : j + i + 1]) > maxx) & (len(s[i : j + i + 1]) == len(set(s[i : j + i + 1]))):
                        maxx = len(s[i : j + i + 1])
                        if maxx == 95:
                            return maxx
            return maxx
