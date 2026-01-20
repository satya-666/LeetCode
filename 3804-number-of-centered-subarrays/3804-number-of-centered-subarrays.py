class Solution(object):
    def centeredSubarrays(self, nums):
        n = len(nums)
        count=0
        for i in range(n):
            for j in range(i,n+1):
                sub = nums[i:j]
                if sum(sub) in sub:
                    count += 1
        return count
        
