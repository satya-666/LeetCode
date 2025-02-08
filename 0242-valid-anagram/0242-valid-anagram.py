class Solution(object):
    def isAnagram(self, s, t):
        return(sorted(s)==sorted(t))

        # s.strip()
        # t.strip()
        # k = len(s)
        # n = len(t)
        # count = 0
        # not_count = 0
        # for i in range(n):
        #     if t[i] in s:
        #         count +=1
        #     else:
        #         not_count+=1

        # return(not_count<1 and k>=count and k==n)

        