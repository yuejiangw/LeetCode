from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff_array = [0] * (n + 1)
        for booking in bookings:
            diff_array[booking[0]] += booking[2]
            if booking[1] < n:
                diff_array[booking[1] + 1] -= booking[2]
        for i in range(1, n + 1):
            diff_array[i] += diff_array[i - 1]
        return diff_array[1:]
