class Solution(object):
    def containsDuplicate(self, nums):
        k = list(set(nums))

        return (not len(k)==len(nums))
        