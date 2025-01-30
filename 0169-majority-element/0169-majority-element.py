class Solution(object):
    def majorityElement(self, nums):
        s = {}

        for i in nums:
            if i in s:
                s[i] += 1  
            else:
                s[i] = 1  

        max_key = max(s, key=s.get)
        max_value = max(s.values())
        # print(max_value)
        if max_value > len(nums)/2:
            return(max_key)
        