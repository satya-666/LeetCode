class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] >= target:
                return(i)
                break
            elif i == len(nums)-1:
                return(len(nums))
                