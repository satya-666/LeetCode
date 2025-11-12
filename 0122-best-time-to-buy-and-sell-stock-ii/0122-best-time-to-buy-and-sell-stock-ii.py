class Solution(object):
    def maxProfit(self, prices):
        dp = [[-1]*2 for _ in range(len(prices))]
        def helper(ind,canBuy):
            profit = 0
            if ind >= len(prices):
                return 0
            if dp[ind][canBuy] != -1:
                return dp[ind][canBuy]
            if canBuy == 1:
                buy = -prices[ind] + helper(ind+1,0)
                notBuy = 0 + helper(ind+1,1)
                profit += max(buy,notBuy)
                dp[ind][canBuy] = profit
            else:
                sell = prices[ind] + helper(ind+1,1)
                notSell = 0 + helper(ind+1,0)
                profit += max(sell,notSell)
                dp[ind][canBuy] = profit
            return profit
        return helper(0,1)