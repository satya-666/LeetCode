class Solution(object):
    def findWordsContaining(self, words, x):
        y = []
        for index, word in enumerate(words):
            if x in word:
                y.append(index)

        return(y)
        