class Solution(object):
    def repairCars(self, ranks, cars):
        def can_repair_all_cars(time):
            total_cars_repaired = 0
            for rank in ranks:
                total_cars_repaired += int((time // rank) ** 0.5)
            return total_cars_repaired >= cars

        left, right = 0, max(ranks) * cars * cars
        while left < right:
            mid = (left + right) // 2
            if can_repair_all_cars(mid):
                right = mid
            else:
                left = mid + 1
        return left
            