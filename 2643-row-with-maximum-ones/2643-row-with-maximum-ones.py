class Solution(object):
    def rowAndMaximumOnes(self, mat):
        index = 0
        max_count = 0
        for i in range(len(mat)):
            count = 0
            for j in range(len(mat[i])):
                if mat[i][j]==1:
                    count += 1
                if count>max_count:
                    max_count=count
                    index=i
        return([index,max_count])

        