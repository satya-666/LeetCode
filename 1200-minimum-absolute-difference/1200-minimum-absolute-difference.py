class Solution(object):
    def minimumAbsDifference(self, arr):
        n = len(arr)
        arr.sort()
        nums = []
        d = arr[1]-arr[0]
        for i in range(1,n):
            if abs(arr[i]-arr[i-1]) < d:
                d = abs(arr[i]-arr[i-1])
        for j in range(1,n):
            if abs(arr[j]-arr[j-1]) == d:
                nums.append([arr[j-1],arr[j]])
        return nums