class Solution(object):
    def maxAscendingSum(self, nums):
        kim =nums[0]
        sim =nums[0]


        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                sim += nums[i]
            else:
                kim = max(kim, sim)
                sim = nums[i]

        kim = max(kim, sim)

        return(kim)  
        