import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        res = re.search(p,s)

        return res.span()[-1] - res.span()[0] == len(s) if res else False
