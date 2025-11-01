class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        count = 0
        i,j = 0 , 0
        while (i<len(g)) and (j<len(s)):
            if s[j] >= g[i]:
                count += 1
                i+=1
                j+=1
            else:
                j+=1
        return(count)