class Solution(object):
    def smallestRepunitDivByK(self, k):
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        remainder = 0
        for length in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k
            
            if remainder == 0:
                return length
        
        return -1

        # if k % 2 == 0:
        #     return -1
        # else:
        #     n = '1'
        #     while int(n) % k != 0:
        #         n += str(1)
        #     return len(n)
