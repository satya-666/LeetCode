class Solution(object):
    def maxAbsoluteSum(self, nums):
        max_sum = 0
        current_sum = 0
        
        for num in nums:
            current_sum += num
            max_sum = max(max_sum, abs(current_sum))
            
            if current_sum < 0:
                current_sum = 0
        
        current_sum = 0  
        for num in nums:
            current_sum += -num
            max_sum = max(max_sum, abs(current_sum))
            
            if current_sum < 0:
                current_sum = 0
        
        return max_sum
        