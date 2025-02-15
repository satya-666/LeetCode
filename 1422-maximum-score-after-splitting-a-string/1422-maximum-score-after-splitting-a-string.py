class Solution(object):
    def maxScore(self, s):
        n = len(s)
        zero_count = 0
        right_ones = s.count('1')  
        max_score = 0

        for i in range(n - 1):
            if s[i] == '0':
                zero_count += 1
            if s[i] == '1':
                right_ones -= 1

            score = zero_count + right_ones
            max_score = max(max_score, score)

        return max_score