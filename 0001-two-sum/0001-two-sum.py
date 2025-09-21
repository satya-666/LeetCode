class Solution(object):
    def twoSum(self, nums, target):
        # n = len(nums)
        # i, j = 0, n - 1
        # while i < j: 
        #     if nums[i] + nums[j] == target:
        #         return [i, j]
        #     elif nums[i] + nums[j] > target:
        #         j -= 1
        #     else:
        #         i += 1

        hashMap = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in hashMap:
                return [index, hashMap[diff]]
            else:    
                hashMap[value] = index