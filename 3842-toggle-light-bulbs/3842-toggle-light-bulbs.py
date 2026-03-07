class Solution(object):
    def toggleLightBulbs(self, bulbs):
        d = {}
        for i in bulbs:
            if i in d :
                d[i] += 1
            else:
                d[i] = 1
        arr = []
        for key,val in d.items():
            if val % 2 == 1:
                arr.append(key)
        return sorted(arr)