class Solution(object):
    def subsets(self, nums):
        n = len(nums)
        res = []
        def helper(ind,ds):
            if ind == n:
                res.append(ds[:])
                return
            # for i in range(ind,n):
            ds.append(nums[ind])
            helper(ind+1,ds)
            ds.pop()
            helper(ind+1,ds)
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
                