class Solution(object):
    def singleNumber(self, nums):
        nums.sort()

        for i in range(0, len(nums) - 1, 2):
            if nums[i] != nums[i + 1]:
                return(nums[i])
                break
        else:
            return(nums[-1])

        