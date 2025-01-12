class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        for j in range(k):
            n = min(nums)
            i = nums.index(n)
            nums[i]=n*multiplier

        return(nums)
        