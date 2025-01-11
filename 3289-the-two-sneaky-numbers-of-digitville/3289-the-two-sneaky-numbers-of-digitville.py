class Solution(object):
    def getSneakyNumbers(self, nums):
        s = {}
        lst = []

        for i in nums:
            if i in s:
                s[i] += 1
            else:
                s[i] = 1


        l1 = s.values()
        a = list(l1)
        l2 = s.keys()
        b = list(l2)

        kim = []
        for item1, item2 in zip(a, b):
            if item1 ==2 :
                kim.append(item2)
        return(kim)
        