class Solution(object):
    def divideArray(self, nums):
        dic = {}

        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        t = 0
        f = 0
        for key, value in dic.items():
            if value % 2 == 0:
                t+=1
            else:
                f+=1
        return(f<=0)
