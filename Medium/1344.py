class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # Math
        # T, S: O(1)
        minute_angle = (minutes / 60) * 360
        
        base_hour_angle = (hour % 12) * 30
        add_angle = (minutes / 60) * 30
        hour_angle = base_hour_angle + add_angle

        res = abs(minute_angle - hour_angle)
        return res if res < 180 else 360 - res