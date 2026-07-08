class Solution(object):
    def angleClock(self, hour, minutes):
        a = (30*hour) - (5.5*minutes)
        return min(abs(a),abs(360-abs(a)))
        # hour_angle = (hour % 12) * 30 + minutes * 0.5
        # minute_angle = minutes * 6
        # diff = abs(hour_angle - minute_angle)
        # return min(diff, 360 - diff)