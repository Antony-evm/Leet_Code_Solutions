# Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i = 0
        while left != right:
            left >>= 1
            right >>= 1
            i += 1
        return right << i


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while right > left:
            right = right & right - 1
        return left & right
