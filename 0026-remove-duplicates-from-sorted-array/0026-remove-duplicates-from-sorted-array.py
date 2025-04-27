class Solution(object):
    def removeDuplicates(self, nums):
        # k=set(nums)
        # return(len(k))
        i, j = 0, 1
        while j < len(nums):
            if nums[i] == nums[j]:
                nums.pop(j)
            else:
                i += 1
                j += 1 

        return(len(nums))
                