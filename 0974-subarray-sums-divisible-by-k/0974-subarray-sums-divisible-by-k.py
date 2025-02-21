class Solution(object):
    def subarraysDivByK(self, nums, k):
        prefix_sum = 0
        count = {0: 1}
        result = 0

        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k
            if mod < 0:
                mod += k
            if mod in count:
                result += count[mod]
            if mod not in count:
                count[mod] = 0
            count[mod] += 1

        return(result)

        