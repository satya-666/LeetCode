class Solution(object):
    def mergeAlternately(self, word1, word2):
        max_len = max(len(word1), len(word2))
        word1 = word1.ljust(max_len)
        word2 = word2.ljust(max_len)

        kim = ''.join(i + j for i, j in zip(word1, word2))

        return(kim.replace(" ", ""))
        # kim = ""

        # for i, j in zip(word1.ljust(len(word2)), word2.ljust(len(word1))):
        #     kim += i
        #     kim += j

        # return(kim.replace(" ", ""))
