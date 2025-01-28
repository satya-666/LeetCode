class Solution(object):
    def gcdOfStrings(self, str1, str2):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def gcd_of_strings(s1, s2):
            if s1 + s2 != s2 + s1:
                return ""
            length = gcd(len(s1), len(s2))
            return s1[:length]

        result = gcd_of_strings(str1, str2)
        return(result)