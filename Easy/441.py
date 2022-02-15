import math


class Solution:
    def arrangeCoins(self, n: int) -> int:
        """ 模拟, O(N) """
        total = 0
        i = 0
        while total < n:
            total += (i + 1)
            i += 1
        return i if total == n else i - 1

    def arrangeCoins(self, n: int) -> int:
        """ 数学, O(1) """
        return math.floor((-1 + math.sqrt(1 + 8 * n)) / 2)

    
    def arrangeCoins(self, n: int) -> int:
        """ 二分, O(logN) """
        if n == 1:
            return 1
        i, j = 1, n
        while i <= j:
            mid = i + (j - i) // 2
            total = mid * (1 + mid) // 2
            if total == n:
                return mid
            elif total < n:
                i = mid + 1
            else:
                j = mid - 1
        return j
