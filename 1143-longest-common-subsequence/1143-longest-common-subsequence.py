class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        n = len(text1)
        m = len(text2)
        dp = [[-1]*(m+1) for _ in range(n+1)]
        def helper(i,j):
            if i >= n or j >= m:
                return 0
            if text1[i] == text2[j]:
                return 1+helper(i+1,j+1)
            if dp[i][j] != -1:
                return dp[i][j]
            ans1 = helper(i+1,j)
            ans2 = helper(i,j+1)
            dp[i][j] = max(ans1,ans2)
            return dp[i][j]
        return helper(0,0)