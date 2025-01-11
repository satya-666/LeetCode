class Solution(object):
    def finalValueAfterOperations(self, operations):
        count = 0
        for i in operations:
            if i == "--X" or i == "X--" :
                count -=1

            if i == "X++" or i == "++X" :
                count += 1
        return(count)
        