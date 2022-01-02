from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window, res = deque(), []
        for i, v in enumerate(nums):
            # 假设窗口的左右边界为 left 和 right，当队列头部的
            # 元素小于 left 时（队列中存的是下标），就应该出队列
            # 由 for 循环和窗口长度为 k 可知，right = i，left = i - k
            # 并且在队列中元素数量小于 k 的时候不用出队列，因此条件为
            # i >= k and window[0] <= i - k
            if i >= k and window[0] <= i - k:
                window.popleft()
            # 单调递减队列，队列头部元素是窗口中的最大值
            while window and nums[window[-1]] <= v:
                window.pop()
            window.append(i)
            if i >= k - 1:
                res.append(nums[window[0]])
        return res