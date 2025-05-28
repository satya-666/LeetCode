class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []

        i = 0
        j = i + 1
        k = len(nums) - 1

        while i < len(nums) - 2:
            if j >= k:
                i += 1
                j = i + 1
                k = len(nums) - 1
                continue

            total = nums[i] + nums[j] + nums[k]

            if total == 0:
                triplet = [nums[i], nums[j], nums[k]]
                if triplet not in result:
                    result.append(triplet)
                j += 1  
                k -= 1  
            elif total < 0:
                j += 1  
            else:
                k -= 1

        return(result)

        