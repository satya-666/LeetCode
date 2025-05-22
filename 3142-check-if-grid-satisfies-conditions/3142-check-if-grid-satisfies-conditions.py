class Solution(object):
    def satisfiesConditions(self, grid):
        t = 0
        f = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):

                if i + 1 < len(grid):
                    if grid[i][j] == grid[i + 1][j]:
                        t = 1
                    if grid[i][j] != grid[i + 1][j]:
                        f = 1

                if j + 1 < len(grid[i]):
                    if grid[i][j] == grid[i][j + 1]:
                        f = 1

        return(f == 0)