class Solution(object):
    def canJump(self, nums):
        step = 0
        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach:
                return False 
                break
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= len(nums) - 1:
                return True
                break
        