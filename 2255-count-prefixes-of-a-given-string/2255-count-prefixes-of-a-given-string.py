class Solution(object):
    def countPrefixes(self, words, s):
        words_dict = {}
        for word in words:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1
                
        count = 0
        for i in range(1,len(s)+1):
            part = s[:i]
            if part in words_dict:
                count += words_dict[part]
        return(count)
