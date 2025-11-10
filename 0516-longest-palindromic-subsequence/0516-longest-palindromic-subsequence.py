class Solution(object):
    def longestsubsequence(self,s,t):
        n = len(s)
        dp = [[-1]*(n+1)for _ in range(n+1)]
        def helper(i,j):
            if i >= n or j >= n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if s[i] == t[j]:
                dp[i][j] = 1 + helper(i+1,j+1)
            else:
                dp[i][j] = max((helper(i+1,j),helper(i,j+1)))
            return dp[i][j]
        return helper(0, 0)
    def longestPalindromeSubseq(self, s):
        t = s[::-1]
        return self.longestsubsequence(s,t)
    
