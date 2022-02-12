class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n

        def pow(x, n):
            if n == 1:
                return x
            elif n % 2 == 0:
                tmp = pow(x, n // 2)
                return tmp * tmp
            else:
                tmp = pow(x, n // 2)
                return tmp * tmp * x

        return pow(x, n)
