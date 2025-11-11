class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        streak = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                streak = max(streak,count)
                count = 0
        streak = max(streak,count)
        return streak