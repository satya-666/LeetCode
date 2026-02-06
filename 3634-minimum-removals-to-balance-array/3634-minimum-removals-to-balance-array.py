class Solution(object):
    def minRemoval(self, nums, k):
        nums.sort()
        n = len(nums)
        left = 0
        max_len = 0
        
        for i in range(n):
            while nums[i] > nums[left] * k:
                left += 1
            max_len = max(max_len, i - left + 1)
        
        return(n - max_len)

        