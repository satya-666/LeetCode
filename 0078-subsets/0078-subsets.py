class Solution(object):
    def subsets(self, nums):
        subsequences = []
        n = len(nums)
        for i in range(0, 1 << n):
            subseq = []
            for j in range(n):
                if i & (1 << j):
                    subseq.append(nums[j])
            subsequences.append(subseq)
        subsequences.sort(key=lambda x: (len(x), x))
        return(subsequences)
                