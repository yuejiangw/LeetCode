from typing import List

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        def check(radis):
            i, j = 0, 0
            while i < len(houses) and j < len(heaters):
                if abs(houses[i] - heaters[j]) > radis:
                    while j < len(heaters) and abs(houses[i] - heaters[j]) > radis:
                        j += 1
                else:
                    i += 1
            return i == len(houses)

        left, right = 0, max(heaters[-1],houses[-1])-min(heaters[0],houses[0])
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
