class Solution(object):
    def maxSubarrayLength(self, nums, k):
        start = 0
        max_len = 0
        freq = {}

        for end in range(len(nums)):
            if nums[end] in freq:
                freq[nums[end]] += 1
            else:
                freq[nums[end]] = 1

            while freq[nums[end]] > k:
                freq[nums[start]] -= 1
                start += 1
            
            max_len = max(max_len, end - start + 1)

        return(max_len)
