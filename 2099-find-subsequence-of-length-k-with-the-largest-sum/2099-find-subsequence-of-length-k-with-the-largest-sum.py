class Solution(object):
    def maxSubsequence(self, nums, k):
        indexed = list(enumerate(nums))
        top_k = sorted(indexed, key=lambda x: x[1], reverse=True)[:k]
        top_k_sorted = sorted(top_k, key=lambda x: x[0])
        result = [val for idx, val in top_k_sorted]

        return(result)