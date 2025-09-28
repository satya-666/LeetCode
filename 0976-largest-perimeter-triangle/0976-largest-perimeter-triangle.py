class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            a, b, c = nums[i], nums[i+1], nums[i+2]
            if b + c > a:
                return a + b + c
        return 0

    # def largestPerimeter(self, nums):
    #     n = len(nums)
    #     maxx = [0]
    #     def helper(ind,ds,maxx):
    #         count = 0
    #         if len(ds) == 3:
    #             if ds[0] + ds[1] > ds[2] and ds[1] + ds[2] > ds[0] and ds[2] + ds[0] > ds[1] :
    #                 count = sum(ds)
    #                 if count > maxx[0]:
    #                     maxx[0] = count
    #             return
    #         if ind >= n:
    #             return
    #         ds.append(nums[ind])
    #         helper(ind+1,ds,maxx)
    #         ds.pop()
    #         helper(ind+1, ds,maxx)

    #     helper(0, [],maxx)
    #     return maxx[0]