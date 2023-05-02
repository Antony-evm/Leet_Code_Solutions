# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        to_find = dict.fromkeys(s1)
        right = len(s1)
        if len(s1) > len(s2):
            return False
        for idx in range(len(s2) - right + 1):
            for letter in to_find.keys():
                if s1.count(letter) != s2[idx : idx + right].count(letter):
                    res = False
                    break
                else:
                    res = True
            if res:
                return res

        return res
