class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        word = sentence.split()
        n = len(word)

        for i in range(n):
            if word[i][0]==searchWord[0]:

                kim = (word[i])
                sim = len(searchWord)
            
                if kim[:sim]==searchWord:
                    return(i+1)
                    break
            if i==len(word)-1:
                return(-1)