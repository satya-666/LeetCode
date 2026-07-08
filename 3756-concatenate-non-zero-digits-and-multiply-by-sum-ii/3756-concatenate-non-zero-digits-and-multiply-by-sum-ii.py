class Solution(object):
    def sumAndMultiply(self, s, queries):
        MOD = 10**9 + 7
        n = len(s)
        prefix = [0] * n
        prefix[0] = int(s[0])

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + int(s[i])

        numberupto = [0] * n
        new = 0
        for i in range(n):
            if s[i] != '0':
                new = (new * 10 + int(s[i])) % MOD
            numberupto[i] = new

        non_zero = [0] * n
        count = 0
        for i in range(n):
            if s[i] != '0':
                count += 1
            non_zero[i] = count

        pow10 = [1] * (count + 1)
        for i in range(1, count + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        res = []

        for l, r in queries:
            if l == 0:
                num = numberupto[r]
                sm = prefix[r]
            else:
                digits = non_zero[r] - non_zero[l - 1]

                num = (
                    numberupto[r]
                    - numberupto[l - 1] * pow10[digits]
                ) % MOD

                sm = prefix[r] - prefix[l - 1]

            val = (num * sm) % MOD
            res.append(val)

        return res