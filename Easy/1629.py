from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str: 
        max_key = keysPressed[0]
        max_duration = releaseTimes[0]
        for i in range(1, len(keysPressed)):
            duration = releaseTimes[i] - releaseTimes[i - 1]
            if duration > max_duration:
                max_duration = duration
                max_key = keysPressed[i]
            if duration == max_duration and keysPressed[i] > max_key:
                max_key = keysPressed[i]
        return max_key
