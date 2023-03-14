# Given an integer number n, return the difference between the product of its digits and the sum of its digits.

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        from itertools import accumulate
        return 0 if n<10 else list(accumulate(str(n),lambda x,y: int(x)*int(y)))[-1] -  list(accumulate(str(n),lambda x,y: int(x)+int(y)))[-1]