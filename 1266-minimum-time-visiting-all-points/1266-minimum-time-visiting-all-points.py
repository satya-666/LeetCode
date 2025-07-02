class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        dist = 0

        for i in range(1,len(points)):

            dist += max(abs(points[i][0]-points[i-1][0]),abs(points[i][1]-points[i-1][1]))

        return(dist)
        