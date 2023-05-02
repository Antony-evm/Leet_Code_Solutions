# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backspace(s, l, r):
            while l < r:
                if s[l] == "#" and l > 0:
                    s = s[: l - 1] + s[l + 1 :]
                    r -= 2
                    l -= 2
                elif s[l] == "#" and l == 0:
                    s = s[l + 1 :]
                    r -= 1
                    l -= 1
                l += 1
            return s

        return backspace(s, 0, len(s)) == backspace(t, 0, len(t))
