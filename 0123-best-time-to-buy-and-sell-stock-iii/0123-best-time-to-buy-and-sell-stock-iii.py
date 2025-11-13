class Solution(object):
    def maxProfit(self, prices):
        dp = {}
        def helper(ind,canBuy,count):
            profit = 0
            if ind >= len(prices) or count >= 2:
                return 0
            if (ind,canBuy,count) in dp:
                return dp[(ind,canBuy,count)]
            if canBuy == 1:
                buy = -prices[ind] + helper(ind+1,0,count)
                notBuy = 0 + helper(ind+1,1,count)
                profit = max(buy,notBuy)
                dp[(ind,canBuy,count)] = profit
            else:
                sell = prices[ind] + helper(ind+1,1,count+1)
                notSell = 0 + helper(ind+1,0,count)
                profit = max(sell,notSell)
                dp[(ind,canBuy,count)] = profit
            return profit
        return helper(0,1,0)
