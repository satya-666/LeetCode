class Solution(object):
    def maxProfit(self, prices):
        count = 0

        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                count += prices[i+1] - prices[i]
        return(count)