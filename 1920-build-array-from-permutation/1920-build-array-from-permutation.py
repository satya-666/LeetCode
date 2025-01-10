class Solution(object):
    def buildArray(self, nums):
        lst = []
        for i in range(len(nums)):
            lst.append(nums[nums[i]])
        return(lst)
        