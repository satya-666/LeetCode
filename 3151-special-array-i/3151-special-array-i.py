class Solution(object):
    def isArraySpecial(self, nums):
        i, j = 0, 1
        t = 0
        f = 0

        if len(nums) == 1:
            return(True)
        else:
            while j < len(nums): 
                if (nums[i] % 2 == 0 and nums[j] % 2 == 1) or (nums[i] % 2 == 1 and nums[j] % 2 == 0):
                    t += 1
                else:
                    f += 1 
                i += 1
                j += 1
            
            return(False if f >= 1 else True)