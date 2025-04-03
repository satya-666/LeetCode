class Solution(object):
    def reverseVowels(self, s):
        t = {'a','e','i','o','u','A','E','I','O','U'}
        i, j = 0, len(s) - 1
        lst = list(s)

        while i < j:
            if lst[i] in t and lst[j] in t:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
                j -= 1
            elif lst[i] not in t:
                i += 1
            else:
                j -= 1

        return("".join(lst))