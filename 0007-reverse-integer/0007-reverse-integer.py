class Solution(object):
    def reverse(self, x):
        if x >= -2147483648 and x <= 2147483647:
            if x >= 0:
                x = str(x)
                res = int(x[::-1])
            else:
                x = str(x)
                res = int(x[0] + x[:0:-1])  
            if res >= -2147483648 and res <= 2147483647:
                return res
        return 0
