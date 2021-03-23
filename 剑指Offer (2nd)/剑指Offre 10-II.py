# 0级台阶有一种跳法
from functools import lru_cache
class Solution:
    """
    使用了LRU缓存机制（最近最少使用）
    对于每个后续函数调用，首先通过查看缓存来检查结果是否已经计算过。
    如果在缓存中找到了，那就很完美，不需要再次计算！如果没有找到，
    就计算结果并将输入和结果存储在缓存中，以便下一个函数调用时查找到它
    """
    @lru_cache(None)
    def numWays(self, n: int) -> int:
        if n <= 1:
            return 1
        return (self.numWays(n - 1) + self.numWays(n - 2)) % 1000000007