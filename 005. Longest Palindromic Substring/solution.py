# Given a string s, return the longest palindromic substring in s.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def is_palindrome(s):
            return s==s[::-1]

        if len(s)==1:
            return s[0]
        
        maxOutput = len(s)

        while maxOutput>1:
            for r in range(len(s)-maxOutput+1):
                if is_palindrome(s[r:maxOutput+r]):
                    return s[r:maxOutput+r]
            maxOutput -=1
        return s[0]