class Solution(object):
    def shortestToChar(self, s, c):
        c_word = [i for i, ch in enumerate(s) if ch == c]
        result = []
        k = 0
        for j in range(len(s)):
            if s[j] == c:
                result.append(0)
            else:
                while k < len(c_word) - 1 and abs(c_word[k+1] - j) < abs(c_word[k] - j):
                    k += 1
                result.append(abs(c_word[k] - j))
        return result
