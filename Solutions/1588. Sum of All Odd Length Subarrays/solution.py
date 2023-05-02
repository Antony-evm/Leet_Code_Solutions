# Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.

# A subarray is a contiguous subsequence of the array.


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        for sublen in range(1, len(arr) + 1, 2):
            idx = 0
            while idx < len(arr) - sublen + 1:
                res += sum(arr[idx : idx + sublen])
                idx += 1

        return res
