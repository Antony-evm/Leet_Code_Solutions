# Given two binary strings a and b, return their sum as a binary string.


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        res, carry = "", "0"
        for i, j in zip_longest(a, b):
            if not i:
                i = 0
            if not j:
                j = 0
            total = int(i) + int(j) + int(carry)
            if total == 3:
                res = "1" + res
                carry = "1"
            elif total == 2:
                res = "0" + res
                carry = "1"
            elif total == 1:
                res = "1" + res
                carry = "0"
            else:
                res = "0" + res
                carry = "0"
        return carry + res if carry == "1" else res
