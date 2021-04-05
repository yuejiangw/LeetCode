class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(pow(c, 0.5))
        while a <= b:
            if pow(a, 2) + pow(b, 2) == c:
                return True

            if pow(a, 2) + pow(b, 2) < c:
                a += 1
            
            if pow(a, 2) + pow(b, 2) > c:
                b -= 1
        return False 