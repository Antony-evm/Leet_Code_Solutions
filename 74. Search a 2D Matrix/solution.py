You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.



class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = list(chain(*matrix))
        return bisect_left(l,target)!=bisect_left(l,target+1)



class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, m*n-1
        while l <= r:
            mid = l + (r-l)//2
            row = mid // n
            col = mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] <= target:
                l = mid +1
            else:
                r = mid -1
        return False