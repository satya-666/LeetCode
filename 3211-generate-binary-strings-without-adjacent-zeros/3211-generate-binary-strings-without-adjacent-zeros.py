class Solution(object):
    def validStrings(self, n):
        result = []
        for i in range(2 ** n):
            s = bin(i)[2:].zfill(n)
            if "00" not in s:
                result.append(s)
        return result



