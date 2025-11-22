class Solution(object):
    def minimumOperations(self, nums):
        count = len(nums)
        for i in nums:
            if i % 3 == 0:
                count -= 1
        return(count)
        