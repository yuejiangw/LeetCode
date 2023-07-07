from typing import List


class Solution:
    def dietPlanPerformance(
        self, calories: List[int], k: int, lower: int, upper: int
    ) -> int:
        """
        翻译一下题目，窗口长度固定为 k，扫描整个数组不断移动窗口，如果发现窗口内的值的和大于 upper 则把结果加 1 分，
        窗口内值的总和小于 lower 则结果减一分，否则结果不变
        """
        l, r = 0, 0
        window = 0
        window_size = 0
        res = 0
        while r < len(calories):
            # 窗口扩张
            c = calories[r]
            r += 1
            window += c
            window_size += 1
            # 窗口收缩
            if window_size > k:
                d = calories[l]
                l += 1
                window -= d
                window_size -= 1
            # 更新结果
            if window_size == k:
                if window > upper:
                    res += 1
                elif window < lower:
                    res -= 1
        return res
