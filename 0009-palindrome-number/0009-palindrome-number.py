class Solution(object):
    def isPalindrome(self, x):
        new = str(x)
        kim = (len(new))
        
        return(new==new[::-1])
        """
        :type x: int
        :rtype: bool
        """
        