class Solution(object):
    def sortedSquares(self, nums):
        arr = []
        for i in nums:
            arr.append(i**2)

        return(sorted(arr))
        