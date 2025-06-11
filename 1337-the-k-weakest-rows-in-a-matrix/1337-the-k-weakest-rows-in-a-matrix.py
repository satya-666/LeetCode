class Solution(object):
    def kWeakestRows(self, mat, k):
        strength = []
        for i in range(len(mat)):
            count = sum(mat[i])
            strength.append((count, i))

        strength.sort()

        result = []
        for i in range(k):
            count, index = strength[i]
            result.append(index)

        return(result)
        