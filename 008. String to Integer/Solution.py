import re
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s)==0:
            return 0
        sign = -1 if s[0] == '-' else 1
        s = s[1:] if sign == -1 or s[0]=='+' else s
        if len(s)==0:
            return 0
            
        pattern_found = re.search("[^0-9]",s)
        stop = pattern_found.span()[0] if pattern_found else len(s)+1 
        if stop == 0:
            return 0
        else:
            res = int(s[:stop])*sign
            if sign==-1:
                return res if res.bit_length()<32 else -2**31
            else:
                return res if res.bit_length()<32 else 2**31-1

