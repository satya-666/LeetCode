class Solution(object):
    def findMaxK(self, nums):
        nums.sort()

        i, j = 0, len(nums) - 1
        arr = []
        while i < j:
            if nums[i] + nums[j] == 0:
                arr.append(nums[i])
                arr.append(nums[j])
                i += 1
                j -= 1
            elif nums[i] + nums[j] < 0:
                i += 1
            else:
                j -= 1
        if len(arr)==0:
            return -1
        else:
            return(max(arr))

