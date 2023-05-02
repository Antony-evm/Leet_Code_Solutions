# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.


class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = list(dict.fromkeys(s))
        for char in chars:
            if s.count(char) == 1:
                return s.find(char)

        return -1
