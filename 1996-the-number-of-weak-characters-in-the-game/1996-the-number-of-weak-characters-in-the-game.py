class Solution(object):
    def numberOfWeakCharacters(self, properties):
        properties.sort(key=lambda x:(-x[0],x[1]))

        max_power = 0
        weak = 0
        for i,j in properties:
            if j < max_power:
                weak += 1
            else:
                max_power = j
        return weak