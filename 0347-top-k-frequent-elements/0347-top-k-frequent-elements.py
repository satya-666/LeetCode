class Solution(object):
    def topKFrequent(self, nums, k):
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        n = len(nums)
        bucket = [[] for _ in range(n + 1)]
        for num, freq in freq_map.items():
            bucket[freq].append(num)

        res = []
        for i in range(n, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res