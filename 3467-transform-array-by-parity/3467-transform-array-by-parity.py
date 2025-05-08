class Solution(object):
    def transformArray(self, nums):
        result = []

        for i in range(len(nums)):
            if nums[i]%2==0:
                result.append(0)
            else:
                result.append(1)
        result.sort()
        return(result)