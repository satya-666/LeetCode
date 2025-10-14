class Solution(object):
    def hasIncreasingSubarrays(self, nums, k):
        n = len(nums)
        if k == 1:
            return n >= 2
        count = 1
        starts = []
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                count += 1
            else:
                count = 1
            if count >= k:
                starts.append(i - k + 1)
        starts_set = set(starts)
        for s in starts_set:
            if s + k in starts_set:
                return True
        return False