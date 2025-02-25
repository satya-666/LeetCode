class Solution(object):
    def searchRange(self, nums, target):
        def findLeft(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def findRight(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left = findLeft(nums, target)
        right = findRight(nums, target)
        
        if left <= right:
            return [left, right]
        return [-1, -1]
        