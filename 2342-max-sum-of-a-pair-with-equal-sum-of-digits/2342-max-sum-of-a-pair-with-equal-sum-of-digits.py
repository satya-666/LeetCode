class Solution(object):
    def maximumSum(self, nums):
        sums_dict = {}
        arr = []

        for num in nums:
            digit_sum = sum(int(digit) for digit in str(num))
            
            if digit_sum in sums_dict:
                sums_dict[digit_sum].append(num)
            else:
                sums_dict[digit_sum] = [num]

        for key, value in sums_dict.items():
            if len(value) == 2:
                arr.append(sum(value))  
            elif len(value) > 2:
                arr.append(sum(sorted(value, reverse=True)[:2]))

        if len(arr) == 0:
            return(-1)
        else:
            return(max(arr)) 
        