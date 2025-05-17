class Solution(object):
    def minMoves2(self, nums):
        n = len(nums)
        nums.sort()
        median = nums[n // 2]

        cost = sum(abs(x - median) for x in nums)

        return(cost)
        