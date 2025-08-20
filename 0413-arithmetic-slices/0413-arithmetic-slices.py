class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        if len(nums) < 3:
            return 0
        streak = 0
        count = 0
        diff = nums[1] - nums[0]
        for i in range(1,len(nums)):
            curr_diff = nums[i] - nums[i-1]
            if curr_diff == diff:
                streak += 1
            if curr_diff != diff :
                diff = curr_diff
                streak = 1
            if streak == 2:
                count += 1
            if streak > 2:
                count += streak-1

        return(count)
