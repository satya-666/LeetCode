class Solution(object):
    def minimumDifference(self, nums, k):
        nums.sort(reverse=True)
        selected = nums[:k]
        return selected[0] - selected[-1]
        