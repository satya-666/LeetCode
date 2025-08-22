class Solution(object):
    def partitionString(self, s):
        count = 0
        s_part = ''
        for i in range(len(s)):
            if s[i] in s_part:
                s_part = ''
                s_part += s[i]
                count += 1
            else:
                s_part += s[i]
        if s[-1] in s_part:
            count += 1

        return(count)
                