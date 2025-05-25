class Solution(object):
    def checkXMatrix(self, grid):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i == j or i+j == len(grid)-1) and grid[i][j] == 0:
                    count+=1
                if not (i == j or i + j == len(grid) - 1) and grid[i][j] != 0:
                    count +=1

        return(count==0)
