class Solution(object):
    def minimumBoxes(self, apple, capacity):
        capacity.sort(reverse=True)
        total_apple = sum(apple)
        count = 0
        for i in capacity:
            if total_apple > 0:
                total_apple -= i
                count += 1
            else:
                break
        return count