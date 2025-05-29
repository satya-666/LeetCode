class Solution(object):
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()

        radius = 0
        i = 0 

        for house in houses:
            while i < len(heaters) - 1 and abs(heaters[i+1] - house) <= abs(heaters[i] - house):
                i += 1
            dist = abs(heaters[i] - house)
            radius = max(radius, dist)

        return radius


        