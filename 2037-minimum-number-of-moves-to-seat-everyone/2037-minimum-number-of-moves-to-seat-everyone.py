class Solution(object):
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        
        moves = 0
        for s, st in zip(seats, students):
            moves += abs(s - st)
        
        return moves