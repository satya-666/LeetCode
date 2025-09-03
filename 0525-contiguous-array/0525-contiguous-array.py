class Solution(object):
    def findMaxLength(self, nums):
        n = len(nums)

        res = [0]*n
        for i in range(n):
            if nums[i] == 0:
                res[i] = -1
            else:
                res[i] = 1

        prefix = [0]*n
        prefix[0] = res[0]
        for j in range(1, n):
            prefix[j] = prefix[j-1] + res[j]


        first_seen = {0: -1} 
        max_len = 0

        for i in range(n):
            psum = prefix[i]
            if psum in first_seen:
                max_len = max(max_len, i - first_seen[psum])
            else:
                first_seen[psum] = i

        return(max_len)