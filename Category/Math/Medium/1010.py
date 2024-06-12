from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        """
        假设两个数 a 和 b 能被 60 整除, 则满足 (a + b) % 60 == 0
        我们还可以根据 mod 运算的性质得出: ((a % 60) + (b % 60)) % 60 == 0
        因此用一个长度为 60 的数组来表示余数 (0 - 59), 时间复杂度 O(N)
        空间复杂度 O(1)
        """
        remain = [0] * 60
        res = 0
        for t in time:
            idx = t % 60
            if idx != 0:
                # 如果时间余数不为0，找出相加为0的余数总和
                res += remain[60 - idx]
            else:
                # 如果为0，加上其它为0的数
                res += remain[idx]
            remain[idx] += 1
        return res