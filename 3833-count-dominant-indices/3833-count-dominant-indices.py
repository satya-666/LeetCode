class Solution(object):
    def dominantIndices(self, nums):
        n = len(nums)
        count = 0
        for i in range(n):
            right = n - (i + 1)
            if right == 0:
                continue  
            if nums[i] > sum(nums[i+1:]) / right:
                count += 1
                
        return count
        