from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """思路
        转换为找一个固定大小滑动窗口，使得窗口内的所有元素之和全局最小
        """
        # T: O(N)
        # S: O(1)
        min_value = float('inf')
        i, j = 0, 0
        window_sum = 0
        window_len = len(cardPoints) - k
        while j < len(cardPoints):
            c = cardPoints[j]
            j += 1
            window_sum += c
            while j - i > window_len:
                d = cardPoints[i]
                i += 1
                window_sum -= d

            if j - i == window_len:
                min_value = min(min_value, window_sum)
        return sum(cardPoints) - min_value