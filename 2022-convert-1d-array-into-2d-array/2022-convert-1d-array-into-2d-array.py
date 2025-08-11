class Solution(object):
    def construct2DArray(self, original, m, n):
        null = []
        # matrix = [[0]*n]*m
        matrix = [[0 for _ in range(n)] for _ in range(m)]

        index = 0
        if m*n == len(original):
            for i in range(m):
                for j in range(n):
                    matrix[i][j] = original[index]
                    index += 1

            return(matrix)
        return null