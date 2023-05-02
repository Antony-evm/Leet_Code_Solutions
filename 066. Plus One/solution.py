# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        rp = len(digits) - 1
        res = []

        while rp >= 0:
            num = digits[rp] + carry
            if num > 9:
                num = 0
                carry = 1
            else:
                carry = 0

            rp -= 1
            res.insert(0, num)

        if carry == 1:
            res.insert(0, carry)
        return res
