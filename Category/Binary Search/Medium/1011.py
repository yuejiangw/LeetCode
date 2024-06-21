from typing import List


class Solution:
    def take_time(self, weights, boat_carry_weight):
        time = 1
        current_weight = 0
        for weight in weights:
            current_weight += weight
            if current_weight > boat_carry_weight:
                current_weight = weight
                time += 1
        return time

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        i, j = max(weights), sum(weights) + 1
        while i < j:
            mid = i + (j - i) // 2
            if self.take_time(weights, mid) <= days:
                j = mid
            else:
                i = mid + 1
        return i
