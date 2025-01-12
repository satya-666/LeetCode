class Solution(object):
    def differenceOfSums(self, n, m):
        total_sum = n * (n + 1) // 2


        count_multiples = n // m


        sum_multiples = m * (count_multiples * (count_multiples + 1)) // 2


        sum_not_multiples = total_sum - sum_multiples


        result = sum_not_multiples - sum_multiples
        return(result)
        