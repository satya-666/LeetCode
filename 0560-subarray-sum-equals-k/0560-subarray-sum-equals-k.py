class Solution(object):
    def subarraySum(self, nums, k):
        sum_count = defaultdict(int)
        sum_count[0] = 1
        current_sum = 0
        result = 0
        
        for num in nums:
            current_sum += num
            if current_sum - k in sum_count:
                result += sum_count[current_sum - k]
            sum_count[current_sum] += 1
        
        return result
        
        