class Solution(object):
    def findTheArrayConcVal(self, nums):
        n=len(nums)
        i,j=0,len(nums)-1
        arr = []
        if len(nums)%2!=0:
            arr.append(nums[n//2])
        while i<j:
            arr.append(str(nums[i])+str(nums[j]))
            i+=1
            j-=1

        total = 0
        for i in arr:
            total+= int(i)
        return(total)