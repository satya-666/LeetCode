class Solution(object):
    def maximumLength(self, nums):
        even = [i for i in nums if i % 2 == 0]

        odd = [i for i in nums if i % 2 == 1]

        even_odd = [nums[i] for i in range(len(nums))
                if i == 0 or nums[i] % 2 != nums[i-1] % 2]

        odd_even = [nums[i] for i in range(1, len(nums))
                    if nums[i] % 2 != nums[i-1] % 2]

        return(max(len(even),len(odd),len(even_odd),len(odd_even)))