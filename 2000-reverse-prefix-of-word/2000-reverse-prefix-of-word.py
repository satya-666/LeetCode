class Solution(object):
    def reversePrefix(self, word, ch):
        i = 0

        while i < len(word):
            if word[i] == ch:
                break
            i += 1

        if i == len(word):  
            left = word
            right = ""
        else:
            left = word[:i+1][::-1]  
            right = word[i+1:]  
        return(left + right)
