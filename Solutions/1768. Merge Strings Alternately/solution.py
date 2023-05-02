# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for l1, l2 in zip_longest(word1, word2):
            res = res + l1 if l1 != None else res
            res = res + l2 if l2 != None else res
        return res
