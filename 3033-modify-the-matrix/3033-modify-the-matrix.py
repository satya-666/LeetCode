class Solution(object):
    def modifiedMatrix(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        max_column = [
            max(matrix[i][j] for i in range(rows) if matrix[i][j] != -1)
            for j in range(cols)
        ]

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == -1:
                    matrix[i][j] = max_column[j]

        return(matrix)