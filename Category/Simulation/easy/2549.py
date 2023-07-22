class Solution:
    def distinctIntegers(self, n: int) -> int:
        # 由于 n - 1 一定满足要求，因此不断循环后 [2, n] 都会在桌面上，答案为 n - 1
        # n = 1 时为特殊情况，答案为 1
        return n - 1 if n > 1 else 1
