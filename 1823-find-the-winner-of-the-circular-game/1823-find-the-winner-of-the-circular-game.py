class Solution(object):
    def findTheWinner(self, n, k):
        result = list(range(1, n + 1))
        index = 1 

        i = 0
        while len(result) > 1:
            if index == k:
                result.pop(i)
                index = 1 
                if i == len(result):
                    i = 0
            else:
                i += 1
                if i == len(result):
                    i = 0
                index += 1

        return(result[0])