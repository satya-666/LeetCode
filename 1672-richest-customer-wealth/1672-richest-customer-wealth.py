class Solution(object):
    def maximumWealth(self, accounts):
        maximum = 0
        for customer in accounts:
            customer_wealth = sum(customer)
            if customer_wealth > maximum:
                maximum = customer_wealth
        return maximum

        
        