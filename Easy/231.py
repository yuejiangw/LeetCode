class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 1
        while x < n:
            x = x << 1
        return x == n


class Solution:
    """ 不用递归或循环 """
    def isPowerOfTwo(self, n: int) -> bool:
        return (n > 0) and (n & (n - 1) == 0)
