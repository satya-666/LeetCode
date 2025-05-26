class Solution(object):
    def checkSubarraySum(self, nums, k):
        
        mod_map = {0:-1} 
        prefix_sum = 0

        for i, num in enumerate(nums):
            prefix_sum += num
            mod = prefix_sum % k
            if mod in mod_map:
                if i - mod_map[mod] >= 2:
                    return True
                    break
            else:
                mod_map[mod] = i
        else:
            return False