class Solution(object):
    def isPalindrome(self, s):
        ns = ''
        for ch in s:
            if ch.isalnum(): 
                ns+=(ch.lower())
        n = len(ns)
        def pd(i):
            if i >= n//2:
                return True
            if ns[i] != ns[n-i-1]:
                return False
            return pd(i+1)
        return pd(0)
        # k = []
        # for i in s:
        #     if i.isalnum(): 
        #         k.append(i.lower())

        # start, end = 0, len(k) - 1
        # while start < end:
        #     if k[start] != k[end]:
        #         return(2==3)
        #         break
        #     start += 1
        #     end -= 1
        # else:
        #     return(2==2)
        