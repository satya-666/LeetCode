class Solution(object):
    def subsets(self, nums):
        n = len(nums)
        nums.sort()
        res = []
        def helper(ind,ds):
            if ind <= n:
                res.append(ds[:])
            for i in range(ind,n):
                # if nums[i] == nums[i-1]:
                #     continue
                ds.append(nums[i])
                helper(i+1,ds)
                ds.pop()
        helper(0,[])
        return res
        # subsequences = []
        # n = len(nums)
        # for i in range(0, 1 << n):
        #     subseq = []
        #     for j in range(n):
        #         if i & (1 << j):
        #             subseq.append(nums[j])
        #     subsequences.append(subseq)
        # subsequences.sort(key=lambda x: (len(x), x))
        # return(subsequences)
                