class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        product = 1
        product_without_zero = 1
        count = 0
        for i in nums:
            product *= i
            if i!=0:
                product_without_zero *= i
            if i == 0:
                count+=1

        result = []

        if count >= 2:
            return([0]*n)
        else: 
            for i in range(n):
                if nums[i] == 0:
                    result.append(product_without_zero)
                else:
                    result.append(product//nums[i])

            return(result)
        