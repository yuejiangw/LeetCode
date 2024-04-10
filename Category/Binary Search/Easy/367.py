class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        while left <= right:
            mid = left + (right - left) // 2
            curr = mid * mid
            if curr == num:
                return True
            elif curr < num:
                left = mid + 1
            else:
                right = mid - 1
        return False