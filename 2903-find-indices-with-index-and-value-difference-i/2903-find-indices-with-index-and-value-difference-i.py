class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        if indexDifference == 0 and valueDifference == 0:
            return([0, 0])
        else:
            i = 0
            j = indexDifference
            found = False

            while i < len(nums) - indexDifference:
                j = i + indexDifference 
                while j < len(nums):
                    if abs(nums[i] - nums[j]) >= valueDifference:
                        return([i, j])
                        found = True
                        break  
                    j += 1
                if found:
                    break
                i += 1 

            if not found:
                return([-1, -1])