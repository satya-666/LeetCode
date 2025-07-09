class Solution(object):
    def numOfSubarrays(self, arr):
        MOD = 10**9 + 7

        count = 0
        odd = 0
        even = 1  # prefix sum 0 is even
        prefix = 0

        for num in arr:
            prefix += num
            if prefix % 2 == 0:
                count = (count + odd) % MOD
                even += 1
            else:
                count = (count + even) % MOD
                odd += 1

        return(count)
                