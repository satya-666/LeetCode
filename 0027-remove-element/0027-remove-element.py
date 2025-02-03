class Solution(object):
    def removeElement(self, nums, val):
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] == val:
                nums.pop(l)  
                r -= 1
            else:
                l += 1

        return(len(nums))
        