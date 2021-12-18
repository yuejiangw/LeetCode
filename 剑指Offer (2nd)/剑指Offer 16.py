class Solution:
    def myPow(self, x: float, n: int) -> float:
        is_reverse = False if n > 0 else True

        def pow(x, n):
            if n == 0:
                return 1
            if n % 2 == 1:
                temp = self.myPow(x, n // 2)
                return temp * temp * x
            else:
                temp = self.myPow(x, n // 2)
                return temp * temp

        res = pow(x, abs(n))
        return 1 / res if is_reverse else res