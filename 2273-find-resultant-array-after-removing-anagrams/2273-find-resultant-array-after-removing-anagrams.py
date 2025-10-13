class Solution(object):
    def removeAnagrams(self, words):
        new = [words[0]]
        for i in range(1, len(words)):
            if sorted(words[i]) != sorted(words[i - 1]):
                new.append(words[i])
        return new
