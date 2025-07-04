class Solution(object):
    def separateDigits(self, nums):
        result = []

        for num in nums:
            kim = str(num)
            for i in range(len(kim)):
                result.append(int(kim[i]))

        return(result)
        