class Solution(object):
    def maxProduct(self, nums):
        cur_max = cur_min = res = nums[0]
        for num in nums[1:]:
            temp = cur_max
            cur_max = max(num, num * cur_max, num * cur_min)
            cur_min = min(num, num * temp, num * cur_min)
            res = max(res, cur_max)
        return res