class Solution(object):
    def maxSatisfaction(self, satisfaction):
        satisfaction.sort()
        max_count = float('-inf')    
        while satisfaction:
            count = 0
            for index, value in enumerate(satisfaction, start=1):
                contribution = value * index
                count += contribution 
            max_count = max(max_count, count)
            
            if len(satisfaction) == 1:
                break

            satisfaction.remove(min(satisfaction))
        if max_count < 0:
            return 0
        else:
            return(max_count)

        