# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomLetters = list(dict.fromkeys(ransomNote))
        for letter in ransomLetters:
            if ransomNote.count(letter) > magazine.count(letter):
                return False
        return True
