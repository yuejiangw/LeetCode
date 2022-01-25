class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0
        while n > 1:
            res += n // 2
            if n % 2 == 1:
                n = 1 + (n - 1) // 2
            else:
                n = n // 2
        return res
