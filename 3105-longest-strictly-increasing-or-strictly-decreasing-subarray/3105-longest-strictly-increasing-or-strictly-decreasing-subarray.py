class Solution(object):
    def longestMonotonicSubarray(self, nums):
        inc = 1
        dec = 1
        kim = 1

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                inc += 1
                dec = 1

            elif nums[i] > nums[i + 1]:
                dec += 1
                inc = 1
            else:
                inc = dec = 1
            kim = max(kim, inc, dec)

        return(kim)

        