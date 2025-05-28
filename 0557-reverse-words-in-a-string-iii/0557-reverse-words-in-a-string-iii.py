class Solution(object):
    def reverseWords(self, s):
        result = ""

        l,r = 0,1
        while r < len(s):
            if s[r] == ' ':
                
                result += s[l:r][::-1]
                result += " "
                l = r+1

            r+=1
        result += s[l:][::-1]
        return(result)
        