class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        n = len(s)
        count = 0

        for i in range(n-1,-1,-1):
            if s[i] == ' ':
                break
            else:
                count += 1
                    
        return(count)
                