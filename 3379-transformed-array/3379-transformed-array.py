class Solution(object):
    def constructTransformedArray(self, nums):
        n = len(nums)
        result = [0] * n

        for i in range(n):
            if nums[i] == 0:
                result[i] = 0
            else:
                landing = (i + nums[i]) % n
                result[i] = nums[landing]

        return result