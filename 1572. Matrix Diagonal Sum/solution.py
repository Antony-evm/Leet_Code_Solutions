# Given a square matrix mat, return the sum of the matrix diagonals.

# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        i = diagsum = 0
        ll = len(mat)
        for i in range(ll):
            diagsum+=mat[i][i]
            diagsum+=mat[i][ll-1-i]
            
        return diagsum if ll%2==0 else diagsum - mat[i//2][i//2]