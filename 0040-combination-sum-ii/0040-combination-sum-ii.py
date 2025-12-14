class Solution(object):
    def combinationSum2(self, candidates, target):
        n = len(candidates)
        res = []
        candidates.sort()

        def helper(ind,target,ds):
            if target == 0:
                res.append(ds[:])
                return
            for i in range(ind,n):
                if i > ind and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                ds.append(candidates[i])
                helper(i+1,target-candidates[i],ds)
                ds.pop()
        helper(0,target,[])
        return res