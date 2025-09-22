class Solution(object):
    def maxFrequencyElements(self, nums):
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1


        max_value = max(freq_map.values())
        count = 0

        for val in freq_map.values():
            if val == max_value:
                count += val
        return(count)