class Solution(object):
    def sumAndMultiply(self, n):
        if n <= 0:
            return 0
        s = str(n)
        new = ''
        for i in range(len(s)):
            if s[i] != '0':
                new += s[i]
        count = 0
        for i in new:
            count += int(i)
        return int(new)*count
        