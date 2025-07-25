class Solution(object):
    def maxSum(self, nums):
        nums = set(nums)
        result = []
        for i in nums:
            if i >= 0:
                result.append(i)

        if len(result) > 0:
            return sum(result)
        else:
            return max(nums)