from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0

        i = 0
        while i + 1 < len(timeSeries):
            time_slot = timeSeries[i + 1] - timeSeries[i]
            if time_slot < duration:
                res += time_slot
            else:
                res += duration
            i += 1

        res += duration
        return res
