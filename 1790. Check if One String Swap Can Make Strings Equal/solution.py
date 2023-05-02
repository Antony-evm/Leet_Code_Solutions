# You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

# Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        elif len(s1) != len(s2):
            return False
        elif all([i in s2 for i in s1]) == False or all([i in s1 for i in s2]) == False:
            return False
        elif all([s1.count(i) == s2.count(i) for i in s1]) == False:
            return False
        else:
            counter = 0
            for idx in range(len(s1)):
                if s1[idx] != s2[idx]:
                    counter += 1
                if counter == 3:
                    return False
            if counter == 1:
                return False
            else:
                return True
