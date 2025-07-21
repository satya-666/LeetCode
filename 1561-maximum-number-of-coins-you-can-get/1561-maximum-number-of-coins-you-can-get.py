class Solution(object):
    def maxCoins(self, piles):
        piles.sort()

        i , j , k = 0 , len(piles)-2, len(piles)-1
        count = 0
        while i < k and j < k:
            count += piles[j]
            i += 1
            j -= 2
            k -= 2

        return(count)