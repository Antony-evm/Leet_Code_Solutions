# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

class Solution:
    def longestPalindrome(self, s: str) -> int:      
        length = len(s)
        values = Counter(s)
        evens = len([i for i in values.values() if i%2==1])
        return length - evens + 1 if evens>1 else length