class Solution(object):
    def subtractProductAndSum(self, n):
        count = 0
        product = 1
        while n > 0:
            digit = n % 10  
            count += digit
            product *= digit
            n //= 10
        return product - count
        
        # x = str(n)
        # count = 0
        # product = 1
        # for i in x:
        #     count += int(i)
        #     product *= int(i) 

        # return(product-count)
        