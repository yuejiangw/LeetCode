from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        """
        由题意得，移动两个位置不需要任何代价，因此奇数位置移动到奇数位置不用代价，
        偶数位置移动到偶数位置不用代价。那么遍历 position 并分别统计奇数偶数的数量，
        相当于把所有奇数位置上的筹码移动到一起，把所有偶数位置上的筹码移动到一起，最后
        比较哪堆筹码比较少，就是结果。
        """
        odd, even = 0, 0
        for idx in position:
            if idx % 2 == 0:
                even += 1
            else:
                odd += 1
        return min(odd, even)