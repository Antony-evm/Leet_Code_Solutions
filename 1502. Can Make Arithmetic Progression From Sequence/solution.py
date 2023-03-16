# A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

# Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr)==2:
            return True
        else:
            arr.sort()
            diff = arr[1]-arr[0]
            for i in range(len(arr)-1):
                if arr[i+1]-arr[i]!=diff:
                    return False
            return True