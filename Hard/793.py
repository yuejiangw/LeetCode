import sys


class Solution:
    """
    首先，此题的思路与 172. tailing zeros 类似，我们可以采用相同的方法
    来获取 n! 的尾数中 0 的个数。题目中问我们尾数中 0 的个数为 k 的数量，
    可以联想到尾数中 0 的个数为 k 的数有一个范围，因此我们可以利用二分搜索
    来找到这个范围的左右边界，之后数量 = 右边界 - 左边界 + 1。
    需要注意的一点是二分搜索时候 high 的初始化，这里我们直接取 Python 可以支持
    的整形范围的最大值，用 sys.maxsize 表示
    """
    def tailing_zeros(self, n):
        res = 0
        divisor = 5
        while divisor <= n:
            res += (n // divisor)
            divisor *= 5
        return res

    def left_boundary(self, k):
        i, j = 0, sys.maxsize
        while i < j:
            mid = i + (j - i) // 2
            if self.tailing_zeros(mid) >= k:
                j = mid
            else:
                i = mid + 1
        return i

    def right_boundary(self, k):
        i, j = 0, sys.maxsize
        while i < j:
            mid = i + (j - i) // 2
            if self.tailing_zeros(mid) <= k:
                i = mid + 1
            else:
                j = mid
        return i - 1

    def preimageSizeFZF(self, k: int) -> int:
        return self.right_boundary(k) - self.left_boundary(k) + 1
