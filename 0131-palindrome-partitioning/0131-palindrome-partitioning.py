class Solution(object):
    def partition(self, s):
        res = []
        def helper(ind,ds):
            if ind == len(s):
                res.append(ds[:])
                return
            for i in range(ind,len(s)):
                cut = s[ind:i+1]
                if cut == cut[::-1]:
                    ds.append(cut)
                    helper(i+1,ds)
                    ds.pop()
        helper(0,[])
        return res