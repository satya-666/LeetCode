class Solution(object):
    def mergeAlternately(self, word1, word2):
        kim = ""

        for i, j in zip(word1.ljust(len(word2)), word2.ljust(len(word1))):
            kim += i
            kim += j

        return(kim.replace(" ", ""))
