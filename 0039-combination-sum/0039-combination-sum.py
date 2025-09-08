class Solution(object):
    def combinationSum(self, candidates, target):
        ans = []
        def helper(ind,target,ds):
            if ind == len(candidates):
                if target == 0:
                    ans.append(ds[:])
                return
            if candidates[ind] <= target:
                ds.append(candidates[ind])
                helper(ind,target-candidates[ind],ds)
                ds.pop()
            helper(ind+1,target,ds)
        helper(0,target,[])
        return ans