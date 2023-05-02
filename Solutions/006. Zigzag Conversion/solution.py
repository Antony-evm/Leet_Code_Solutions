# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"


class Solution:
    def convert(self, s: str, numrows: int) -> str:
        if numrows == 1:
            return s
        line = 0
        pos = 0
        down = True
        res = []
        for i in s:
            res.append((line, pos, i))
            if down and line < numrows - 1:
                line += 1
            elif down and line == numrows - 1:
                down = False
                pos += 1
                line -= 1
            elif not down and line == 0:
                down = True
                line += 1
            elif not down and line > 0:
                line -= 1
                pos += 1
        res.sort()
        return "".join([j[2] for j in res])
