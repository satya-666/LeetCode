class Solution(object):
    def minimumAverage(self, nums):
        nums.sort()
        # return nums
        i,j = 0,len(nums)-1
        averages = []
        while i<j:
            k = nums[i]+nums[j]
            averages.append(float(k))
            i+=1
            j-=1

        return min(averages)/2
