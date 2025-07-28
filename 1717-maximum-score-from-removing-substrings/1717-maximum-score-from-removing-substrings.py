class Solution(object):
    def maximumGain(self, s, x, y):
        s = list(s)
        count = 0

        if x > y:
            ch1, ch2, score1 = 'a', 'b', x
            ch3, ch4, score2 = 'b', 'a', y
        else:
            ch1, ch2, score1 = 'b', 'a', y
            ch3, ch4, score2 = 'a', 'b', x

        stack = []
        for ch in s:
            if stack and stack[-1] == ch1 and ch == ch2:
                stack.pop()
                count += score1
            else:
                stack.append(ch)

        s = []
        for ch in stack:
            if s and s[-1] == ch3 and ch == ch4:
                s.pop()
                count += score2
            else:
                s.append(ch)

        return(count)
