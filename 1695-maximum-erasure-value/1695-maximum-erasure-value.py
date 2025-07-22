class Solution(object):
    def maximumUniqueSubarray(self, nums):
        seen = set()
        l = 0
        max_window_sum = 0
        window_sum = 0

        for r in range(len(nums)):
            while nums[r] in seen:
                seen.remove(nums[l])
                window_sum -= nums[l]
                l += 1
            seen.add(nums[r])
            window_sum += nums[r]
            max_window_sum = max(max_window_sum, window_sum)

        return(max_window_sum)

