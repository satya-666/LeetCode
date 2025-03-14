class Solution(object):
    def setZeroes(self, matrix):
        rows= set()
        col= set()

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    col.add(j)


        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in rows or j in col:
                    matrix[i][j] = 0

        print(matrix)

        