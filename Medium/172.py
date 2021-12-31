class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        两个数的乘积的尾数中能出现0，说明因数能分解出 2 和 5，因此本题转换为
        求一共能将 n 分解出多少对 2 和 5。因为任意一个偶数都可以分解出2，因此
        只考虑 5 即可。
        """
        res = 0
        divisor = 5
        while divisor <= n:
            res += (n // divisor)
            divisor *= 5
        return res
