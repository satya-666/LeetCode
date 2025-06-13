class Solution(object):
    def findPeakElement(self, nums):
        l=0
        h=len(nums)-1
        while (l<h):
            mid=(l+h)//2
            if (nums[mid]>nums[mid+1]):
                h=mid
            elif (nums[mid]<nums[mid+1]):
                l=mid+1
        return l
        