class Solution(object):
    def vowelConsonantScore(self, s):
        c = 0
        v = 0
        vo = ['a','e','i','o','u']
        co = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]

        for i in s:
            if i in vo:
                v += 1
            elif i in co:
                c += 1
        if c > 0:
            return int(floor(v/c))
        return 0