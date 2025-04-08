class Solution(object):
    def makeSmallestPalindrome(self, s):
        n = len(s)
        result =[]
        for k in range(n):
            result.append(s[k])
        i,j = 0,n-1
        while(i<=n//2) and (j>=n//2):
            if result[i]!=result[j]:
                result[i]=result[j]=min(result[i],result[j])
                i+=1
                j-=1
            else:
                i+=1
                j-=1
        palidrome = ''
        for i in result:
            palidrome+=i

        return(palidrome)
        