class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        arr1.sort()
        arr2.sort()
        i, j = 0, 0
        count = 0

        while i < len(arr1):
            while j < len(arr2) and arr2[j] < arr1[i] - d:
                j += 1
            
            if j < len(arr2) and abs(arr1[i] - arr2[j]) <= d:
                i += 1
            else:
                count += 1
                i += 1

        return(count)
                