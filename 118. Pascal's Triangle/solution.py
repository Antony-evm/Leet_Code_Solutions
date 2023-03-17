# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]
        for i in range(1,numRows):
            res = [1]+[None]*(len(output[i-1])-1)+[1]
            for j in range(1,len(res)-1):
                res[j] = output[i-1][j-1]+output[i-1][j]
            output.append(res)
        return output

                