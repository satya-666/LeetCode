class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count = 0

        for i in jewels:
            for j in stones:
                if i in j:
                    count +=1

        return(count)
        