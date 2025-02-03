class Solution(object):
    def majorityElement(self, nums):
        s = {}
        for i in nums:
            if i in s:
                s[i] +=1
            else:
                s[i]=1

        lst = []

        for i,j in s.items():
            if j > len(nums)/3:
                lst.append(i)
        return(lst) 
                