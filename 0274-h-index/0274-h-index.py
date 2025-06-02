class Solution(object):
    def hIndex(self, citations):
        n = len(citations)
        citations.sort()

        Max = 0
        for i in range(n):
            h_candidate = n - i
            if citations[i] >= h_candidate:
                Max = h_candidate
                break
        return(Max)