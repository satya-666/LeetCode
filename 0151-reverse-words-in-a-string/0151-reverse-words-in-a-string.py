class Solution(object):
    def reverseWords(self, s):
        reversed_words = ' '.join(s.split()[::-1])
        return(reversed_words)