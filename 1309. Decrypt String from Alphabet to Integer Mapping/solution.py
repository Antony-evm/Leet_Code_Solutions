# You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:

# Characters ('a' to 'i') are represented by ('1' to '9') respectively.
# Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
# Return the string formed after mapping.

# The test cases are generated so that a unique mapping will always exist.

class Solution:
    def freqAlphabets(self, s: str) -> str:
        right = 3
        res = []
        decrypt = ''
        while s!='':
            if len(s)>=3:
                if s[2]=='#':
                    decrypt+=chr(int(s[:2])+96)
                    s = s[3:]
                else:
                    decrypt+=chr(int(s[0])+96)
                    s = s[1:]
            else:
                decrypt+=chr(int(s[0])+96)
                s = s[1:]

        return decrypt 

