class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort()
        m =len(nums)

        return(nums[m-k])
        