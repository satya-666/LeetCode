class Solution(object):
    def searchMatrix(self, matrix, target):
        found = False  

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == target:
                    return(2==2)
                    found = True
                    break
            if found:
                break
        else:
            return(2==1)
        