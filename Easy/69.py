class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        l = 1
        h = x
        while l <= h:
            m = l + (h - l) // 2
            sqrt = x // m
            if m == sqrt:
                return sqrt
            elif m > sqrt:
                h = m - 1
            else:
                l = m + 1
        return h