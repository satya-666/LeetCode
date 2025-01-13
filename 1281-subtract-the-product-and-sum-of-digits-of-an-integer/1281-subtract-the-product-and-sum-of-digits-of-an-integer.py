class Solution(object):
    def subtractProductAndSum(self, n):
        x = str(n)
        count = 0
        product = 1
        for i in x:
            count += int(i)
            product *= int(i) 

        return(product-count)
        