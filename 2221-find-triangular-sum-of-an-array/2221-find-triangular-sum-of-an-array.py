class Solution(object):
    def triangularSum(self, nums):
        n = len(nums)
        while n > 1:
            res = [0] * (n - 1)
            for i in range(n - 1):
                res[i] = (nums[i] + nums[i + 1]) % 10
            nums = res
            n = len(nums)
        return nums[0]
