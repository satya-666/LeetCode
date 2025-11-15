class Solution(object):
    def peakIndexInMountainArray(self, arr):
        peak_index = 1

        for i in range(1,len(arr)):
            if arr[i] > arr[i-1]:
                peak_index = i
        return(peak_index)
                