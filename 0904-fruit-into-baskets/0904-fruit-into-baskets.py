class Solution(object):
    def totalFruit(self, fruits):
        count = {}
        start = 0
        max_len = 0

        for i in range(len(fruits)):
            fruit = fruits[i]
            if fruit in count:
                count[fruit] += 1
            else:
                count[fruit] = 1

            while len(count) > 2:
                start_fruit = fruits[start]
                count[start_fruit] -= 1
                if count[start_fruit] == 0:
                    del count[start_fruit]
                start += 1

            max_len = max(max_len, i - start + 1)
        return(max_len)
        