class Solution(object):
    def sortedSquares(self, nums):
        i,j = 0,len(nums)-1

        while i <= j:
            if nums[i]**2 < nums[j]**2:
                nums[i]=nums[i]**2
                i+=1
            else:
                nums[j]=nums[j]**2
                j-=1

        return sorted(nums)


            
