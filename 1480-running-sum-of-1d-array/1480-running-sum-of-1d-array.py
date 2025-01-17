class Solution(object):
    def runningSum(self, nums):
        arr = [0]*len(nums)

        for i in range(len(nums)):
            arr[i]=arr[i-1]+nums[i]
        return(arr)