class Solution(object):
    def rearrangeArray(self, nums):
        changed = True
        while changed:
            changed = False
            for i in range(1, len(nums) - 1):
                if (nums[i - 1] + nums[i + 1]) // 2 == nums[i]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    changed = True 
        return(nums)
                