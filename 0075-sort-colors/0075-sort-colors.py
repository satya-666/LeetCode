class Solution(object):
    def sortColors(self, nums):
        n = len(nums)

        for _ in range(n):
            for i in range(n-1):
                if nums[i]>nums[i+1]:
                    nums[i],nums[i+1]=nums[i+1],nums[i]

        return(nums)

        