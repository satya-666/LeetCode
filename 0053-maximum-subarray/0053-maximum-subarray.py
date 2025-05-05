class Solution(object):
    def maxSubArray(self, nums):
        maxx = float('-inf')
        current = 0

        for i in range(len(nums)):
            current+=nums[i]
            maxx = max(maxx,current)

            if current < 0:
                current = 0
        return(maxx)
                
        