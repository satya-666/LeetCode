class Solution(object):
    def firstPalindrome(self, words):
        for i in range(len(words)):
            n_words=(words[i])
            if n_words==n_words[::-1]:
                return(n_words)
                break
        return("")