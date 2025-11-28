class Solution(object):
    def maxSubarraySum(self, nums, k):
        prefix = 0
        best = float("-inf")
        best_prefix = {}

        for i, num in enumerate(nums):
            prefix += num
            r = (i + 1) % k

            if r in best_prefix:
                best = max(best, prefix - best_prefix[r])

            if r not in best_prefix:
                best_prefix[r] = prefix
            else:
                best_prefix[r] = min(best_prefix[r], prefix)

            if (i + 1) % k == 0:
                best = max(best, prefix)

        return best
        # res = []

        # def helper(i, j):
        #     if j == len(nums):
        #         return
        #     if len(nums[i:j+1]) % k == 0  :
        #         res.append(nums[i:j+1])
        #     helper(i, j+1)

        # for i in range(len(nums)):
        #     helper(i, i)
        # # print(res)
        # max_len = []
        # maxx = float('-inf')
        # for i in range(len(res)):
        #     if len(res[i]) > len(max_len) and maxx < sum(res[i]):
        #         maxx = sum(res[i])
        #         max_len = res[i]
        # # print(max_len)
        # return sum(max_len)