class Solution(object):
    def returnToBoundaryCount(self, nums):
        arr = [0]*len(nums)
        count = 0
        for i in range(len(nums)):
            arr[i]=arr[i-1]+nums[i]
        for i in arr:
            if i == 0:
                count +=1
        return(count)
        