class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i, j = 0, num + 1
        while i < j:
            mid = i + (j - i) // 2
            p = mid * mid
            if p == num:
                return True
            elif p < num:
                i = mid + 1
            else:
                j = mid
        return False
