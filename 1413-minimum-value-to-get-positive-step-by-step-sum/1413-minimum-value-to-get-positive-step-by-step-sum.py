class Solution(object):
    def minStartValue(self, nums):
        lst = [0] * len(nums)

        lst[0] = nums[0]

        for i in range(1, len(nums)):
            lst[i] = lst[i-1] + nums[i]

        min_val = min(lst)

        if min_val > 0:
            return(1)
        else:
            return(abs(min_val) + 1)
