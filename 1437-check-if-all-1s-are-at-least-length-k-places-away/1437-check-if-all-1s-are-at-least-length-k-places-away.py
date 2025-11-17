class Solution(object):
    def kLengthApart(self, nums, k):
        prev = -10**9
        for i, v in enumerate(nums):
            if v == 1:
                if i - prev - 1 < k:
                    return False
                prev = i
        return True