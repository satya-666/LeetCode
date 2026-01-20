class Solution(object):
    def centeredSubarrays(self, nums):
        n = len(nums)
        res = 0
        for i in range(n):
            s = 0
            freq = {}
            for j in range(i, n):
                s += nums[j]
                if nums[j] in freq:
                    freq[nums[j]] += 1
                else:
                    freq[nums[j]] = 1
                if s in freq and freq[s] > 0:
                    res += 1
        return res

        # n = len(nums)
        # count=0
        
        # for i in range(n):
        #     for j in range(i,n+1):
        #         sub = nums[i:j]
        #         if sum(sub) in sub:
        #             count += 1
        # return count
        
