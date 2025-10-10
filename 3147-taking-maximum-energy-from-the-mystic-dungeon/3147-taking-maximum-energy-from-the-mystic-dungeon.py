class Solution(object):
    def maximumEnergy(self, energy, k):
        n = len(energy)
        dp = energy[:] 

        for i in range(n - 1, -1, -1):
            if i + k < n:
                dp[i] += dp[i + k]
        
        return max(dp)

    # def maximumEnergy(self, energy, k):
    #     maxx = float('-inf')
    #     n = len(energy)
    #     m = 0
    #     while m < n:
    #         count = 0
    #         for i in range(m,n,k):
    #             # print(i)
    #             count += energy[i]
    #         if count > maxx:
    #             maxx = count
    #         # print(maxx)
    #         m += 1
    #     return maxx
