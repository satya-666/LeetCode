class Solution(object):
    def sortArrayByParity(self, nums):
        i,j = 0,len(nums)-1

        while i<j:
            if  nums[i]%2==0:
                i+=1
            elif nums[j]%2==1:
                j-=1

            nums[i],nums[j]=nums[j],nums[i]
        return(nums)