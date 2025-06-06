class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        n = len(nums)
        result = [0]*n
        i,j = 0 ,1
        count = 0
        while i < n:
            if nums[i] > nums[j]:
                count += 1
            if j == n-1:
                result[i] = count
                count = 0
                i += 1
                j = 0
            else:
                j += 1
        return(result)
        

        