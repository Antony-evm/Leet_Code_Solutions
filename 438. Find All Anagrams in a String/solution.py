# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        length = len(p)
        p = sorted(p)
        if length > 1:
            potential = [idx for idx,letter in enumerate(s[:-length+1]) if letter in p]
        if length == 1:
            return [idx for idx,letter in enumerate(s) if letter in p]
        res = []
        for idx,idx_string in enumerate(potential):
            if p == sorted(s[idx_string:idx_string+length]):
                res.append(idx_string)
        return res
