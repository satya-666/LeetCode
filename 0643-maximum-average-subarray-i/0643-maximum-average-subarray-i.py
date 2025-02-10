class Solution(object):
    def findMaxAverage(self, nums, k):
        n = len(nums)
        total = sum(nums[:k])
        max_avg = float(total) / k

        for i in range(1, n - k + 1):
            total = total - nums[i - 1] + nums[i + k - 1]
            avg = float(total) / k  
            if avg > max_avg:
                max_avg = avg

        return max_avg

        