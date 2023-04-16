# Given a m x n binary matrix mat, find the 0-indexed position of the row that contains the maximum count of ones, and the number of ones in that row.

# In case there are multiple rows that have the maximum count of ones, the row with the smallest row number should be selected.

# Return an array containing the index of the row, and the number of ones in it.

# m == mat.length 
# n == mat[i].length 
# 1 <= m, n <= 100 
# mat[i][j] is either 0 or 1.

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        my_dict = {i:Counter(mat[i])[1] for i in range(len(mat))}
        key = max(my_dict,key=my_dict.get)
        
        return [key,my_dict[key]]
        