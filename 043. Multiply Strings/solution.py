# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 
class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        conversion = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
        }
        n1 = 0
        n2 = 0
        for i in range(len(num1)):
            n1 += conversion[num1[i]]*(10**(len(num1)-i-1)) 
        for i in range(len(num2)):
            n2 += conversion[num2[i]]*(10**(len(num2)-i-1)) 

        product = n1*n2
        if product < 10:
            return list(conversion.keys())[list(conversion.values()).index(product)]
        product_string = ""

        tracker = 0
        magnitude_tracker = 1

        while 10**(magnitude_tracker - 1) < product:
            column = product%(10**magnitude_tracker) - tracker
            tracker = column
            product_string = list(conversion.keys())[list(conversion.values()).index(column//(10**(magnitude_tracker - 1)))] + product_string
            magnitude_tracker += 1

        return product_string