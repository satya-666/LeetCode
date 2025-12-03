class Solution(object):
    def maxSumDivThree(self, nums):
        nums.sort()
        total = sum(nums)
        rem = total % 3

        if rem == 0:
            return(total)
        else:
            best = 0

            for x in nums:
                if x % 3 == rem:
                    best = max(best, total - x)
                    break   

            target = (3 - rem) % 3
            pair = [x for x in nums if x % 3 == target]

            if len(pair) >= 2:
                best = max(best, total - pair[0] - pair[1])

            return(best)