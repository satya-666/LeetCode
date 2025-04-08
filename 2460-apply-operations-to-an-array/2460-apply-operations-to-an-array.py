class Solution(object):
    def applyOperations(self, nums):
        i, j = 0, 1

        while j < len(nums):
            if nums[i] == nums[j]:
                nums[i] = nums[i] * 2
                nums[j] = 0
                i += 1
                j += 1
            else:
                i += 1
                j += 1

        count = nums.count(0)
        nums = [i for i in nums if i != 0]
        for i in range(count):
            nums.append(0)
        return(nums)
