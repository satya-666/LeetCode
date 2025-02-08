class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        char_set = set()
        count = 0
        l = 0

        for i in range(n):
            while s[i] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[i])
            count = max(count, i - l + 1)

        return(count) 