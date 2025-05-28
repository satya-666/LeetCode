class Solution(object):
    def countBinarySubstrings(self, s):
        counts = []
        count = 1
        count_string = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                counts.append(count)
                count = 1
        counts.append(count)
        for i in range(len(counts)-1):
            count_string+=min(counts[i],counts[i+1])

        return(count_string)
