class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        seenA = set()
        seenB = set()
        result = []
        common = 0

        for i in range(len(A)):
            seenA.add(A[i])
            seenB.add(B[i])

            if A[i] in seenB:
                common += 1
            if B[i] in seenA and A[i] != B[i]:
                common += 1

            result.append(common)

        return(result) 