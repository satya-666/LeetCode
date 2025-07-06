class Solution(object):
    def findPeaks(self, mountain):
        result = []

        i,j,k = 0,1,2

        while k < len(mountain):
            if mountain[i] < mountain[j] > mountain[k]:
                result.append(j)
            i += 1
            j += 1
            k += 1

        return(result)

        