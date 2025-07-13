class Solution(object):
    def findMatrix(self, nums):
        freq_nums = {}
        for i in nums:
            if i in freq_nums:
                freq_nums[i] += 1
            else:
                freq_nums[i] = 1

        kim = max(freq_nums.values())

        arrays = [[] for _ in range(kim)]

        next_slot = {num: 0 for num in freq_nums}

        for num in nums:
            idx = next_slot[num]
            arrays[idx].append(num)
            next_slot[num] += 1

        return(arrays)
