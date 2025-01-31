class Solution(object):
    def isPalindrome(self, s):
        k = []
        for i in s:
            if i.isalnum(): 
                k.append(i.lower())

        start, end = 0, len(k) - 1
        while start < end:
            if k[start] != k[end]:
                return(2==3)
                break
            start += 1
            end -= 1
        else:
            return(2==2)
        