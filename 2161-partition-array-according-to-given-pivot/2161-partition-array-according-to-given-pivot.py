class Solution(object):
    def pivotArray(self, nums, pivot):
        s_pivot = []
        g_pivot = []
        e_pivot = []

        for i in range(len(nums)):
            if  nums[i] < pivot:
                s_pivot.append(nums[i])
            elif nums[i] == pivot:
                e_pivot.append(nums[i])
            else:
                g_pivot.append(nums[i])

        return(s_pivot+e_pivot+g_pivot)
