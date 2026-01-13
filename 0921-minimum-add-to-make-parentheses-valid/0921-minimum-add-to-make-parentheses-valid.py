class Solution(object):
    def minAddToMakeValid(self, s):
        openn = 0
        close = 0

        for i in s:
            if i == '(':
                openn += 1
            elif i == ')' and openn > 0:
                openn -= 1
            else:
                close += 1
        return(openn+close)

        

