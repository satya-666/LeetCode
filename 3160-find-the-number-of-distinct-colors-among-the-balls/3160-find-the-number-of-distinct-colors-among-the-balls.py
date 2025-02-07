from collections import defaultdict

class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        colors_freq = defaultdict(int)
        balls_to_colors = dict()
        sol = [0]*len(queries)
        
        for i, (ball, color) in enumerate(queries):
            if ball in balls_to_colors:
                prev_color = balls_to_colors[ball]
                colors_freq[prev_color] -= 1
                if colors_freq[prev_color] == 0:
                    del colors_freq[prev_color]
            
            balls_to_colors[ball] = color
            if color in colors_freq:
                colors_freq[color] += 1
            else:
                colors_freq[color] = 1
            
            sol[i] = len(colors_freq)
        
        return sol
