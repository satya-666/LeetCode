class Solution(object):
    def missingNumber(self, nums):
        lst=[]
        m = max(nums)
        for i in  range(m+1):
            lst.append(i)
        if len(nums)==len(lst):
            return(m+1)
        for i in lst:
            if i not in nums:
                return(i)