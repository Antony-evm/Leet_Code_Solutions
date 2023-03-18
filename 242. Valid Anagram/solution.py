# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set1,set2 = set(s),set(t)
        if len(set1)!=len(set2) or len(s)!=len(t):
            return False
        for letter in set1:
            if s.count(letter)!=t.count(letter):
                return False
        return True