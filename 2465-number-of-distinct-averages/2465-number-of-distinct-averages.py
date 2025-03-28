class Solution(object):
    def distinctAverages(self, nums):
        nums.sort()
        i,j=0,len(nums)-1
        avg_nums = []
        while i<j:
            avg = (nums[i]+nums[j])
            avg_nums.append(float(avg)/2)
            i+=1
            j-=1
        kim = set(avg_nums)
        return len(kim)