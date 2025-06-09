class Solution(object):
    def isPerfectSquare(self, num):
        num1 = int(num**0.5)

        return(num1**2 == num)
        