class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid)
        freq = {}
        
        for row in grid:
            for val in row:
                freq[val] = freq.get(val, 0) + 1

        a = b = -1
        for num in range(1, n * n + 1):
            count = freq.get(num, 0)
            if count == 2:
                a = num  
            elif count == 0:
                b = num  

        return [a, b]
                    