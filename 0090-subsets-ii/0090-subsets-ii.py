class Solution(object):
    def subsetsWithDup(self, nums):
        n = len(nums)
        nums.sort()
        res = []
        def helper(ind,ds):
            if ind <= n:
                res.append(ds[:])
            for i in range(ind,n):
                if i > ind and nums[i] == nums[i-1]:
                    continue
                ds.append(nums[i])
                helper(i+1,ds)
                ds.pop()
        helper(0,[])
        return res
