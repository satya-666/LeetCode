class Solution(object):
    def minimumIndex(self, capacity, itemSize):
        min_capacity = float('inf')
        index = -1

        for i in range(len(capacity)):
            if capacity[i] >= itemSize and capacity[i] < min_capacity:
                min_capacity = capacity[i]
                index = i

        return index