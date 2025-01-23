class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        min_sum = float('inf')

        for size in range(l, r + 1):
            for i in range(len(nums) - size + 1):
                subarray = nums[i:i + size]
                subarray_sum = sum(subarray)
                if subarray_sum > 0:
                    min_sum = min(min_sum, subarray_sum)

        if min_sum == float('inf'):
            return(-1)
        else:
            return(min_sum)

        