class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        result = []

        num_set = set(nums)
        for i in range(1, n + 1):
            if i not in num_set:
                result.append(i)

        return(result)