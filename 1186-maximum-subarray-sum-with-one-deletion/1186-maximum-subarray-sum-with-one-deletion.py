class Solution(object):
    def maximumSum(self, arr):
        n = len(arr)

        forward = [0] * n
        backward = [0] * n

        forward[0] = arr[0]
        for i in range(1, n):
            forward[i] = max(arr[i], forward[i - 1] + arr[i])

        backward[-1] = arr[-1]
        for i in range(n - 2, -1, -1):
            backward[i] = max(arr[i], backward[i + 1] + arr[i])

        max_sum = max(forward)  

        for i in range(1, n - 1):
            max_sum = max(max_sum, forward[i - 1] + backward[i + 1])

        return(max_sum)

        