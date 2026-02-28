class Solution(object):
    def minimumCost(self, nums):
        inc = nums[0]
        nums = nums[1:]
        f_min = min(nums)
        nums.remove(f_min)
        s_min = min(nums)
        return inc + f_min + s_min
