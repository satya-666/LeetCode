class Solution(object):
    def isSubsequence(self, s, t):
        new = ''
        i,j=0,0

        while (i<len(s)) and (j<len(t)):
            if s[i]==t[j]:
                new+=s[i]
                i+=1
                j+=1
            elif s[i]!=t[j]:
                j+=1
            if j==len(t):
                i+=1
                j=0
        return(s==new)
    
        