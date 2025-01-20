class Solution(object):
    def longestPalindrome(self, s):
        start = 0
        end = len(s) - 1
        k = ""

        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            palindrome1 = s[left+1:right]
            if len(palindrome1) > len(k):
                k = palindrome1

            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            palindrome2 = s[left+1:right]
            if len(palindrome2) > len(k):
                k = palindrome2

        return(k)

        