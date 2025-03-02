class Solution(object):
    def diagonalSum(self, mat):
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i==j or i+j==len(mat)-1:
                    count += mat[i][j]
        return(count)
