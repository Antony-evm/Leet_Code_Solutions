# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def merge_iter(arr, temp, frm, mid, to):
            k = frm
            i = frm
            j = mid + 1
            while i <= mid and j <= to:
                if arr[i] < arr[j]:
                    temp[k] = arr[i]
                    i = i + 1
                else:
                    temp[k] = arr[j]
                    j = j + 1
                k = k + 1

            while i < len(arr) and i <= mid:
                temp[k] = arr[i]
                k = k + 1
                i = i + 1

            for i in range(frm, to + 1):
                arr[i] = temp[i]

        def bottom_up_merge_sort(arr):
            l = 0
            r = len(arr) - 1
            temp = arr.copy()
            m = 1
            while m <= r - l:
                for i in range(l, r, 2 * m):
                    frm = i
                    mid = i + m - 1
                    to = min(i + 2 * m - 1, r)
                    merge_iter(arr, temp, frm, mid, to)
                m = 2 * m

        bottom_up_merge_sort(nums)
