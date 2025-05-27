class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        count = 0
        prefix_sum = 0
        prefix_counts = {0: 1} 

        for num in nums:
            prefix_sum += num
            if (prefix_sum - goal) in prefix_counts:
                count += prefix_counts[prefix_sum - goal]
            if prefix_sum in prefix_counts:
                prefix_counts[prefix_sum] += 1
            else:
                prefix_counts[prefix_sum] = 1

        return(count)

        