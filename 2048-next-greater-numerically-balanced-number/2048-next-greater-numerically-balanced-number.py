class Solution(object):
    def nextBeautifulNumber(self, n):
        while True:
            new = str(n+1)
            dic = {}
            for i in new:
                dic[i] = dic.get(i, 0) + 1
            
            right = all(int(k) == v for k, v in dic.items())
            
            if right:
                break
            n += 1

        return(n+1)
