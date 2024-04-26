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
    

# 清晰版：把单调队列单独包装成一个类
class MonotonicQueue:
    def __init__(self):
        self.queue = deque()
    
    def pop(self, val: int):
        # 如果 val 和 queue 的队头元素相同则 pop，否则不做任何操作
        if self.queue and val == self.queue[0]:
            self.queue.popleft()

    def push(self, val: int) -> None:
        # 单调减队列，当 val 大于队尾元素的时候要把队尾元素出队列，这样保证队列中装的都是最大值候选人
        while self.queue and val > self.queue[-1]:
            self.queue.pop()
        self.queue.append(val)

    def front(self):
        return self.queue[0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        不能使用 heap 来做，因为 heap 中只能移除堆顶元素，无法满足固定窗口这一条件
        使用单调队列（单调减）来解决
        T: O(N)
        S: O(k)
        """
        queue = MonotonicQueue()
        res = []
        # 先将前 k 个元素放入
        for i in range(k):
            queue.push(nums[i])
        # res 存入第一个窗口的最大值
        res.append(queue.front())
        # 滑动窗口
        for i in range(k, len(nums)):
            # 移除窗口最前面的元素
            queue.pop(nums[i - k])
            # 窗口最右边元素入队列
            queue.push(nums[i])
            # 存结果
            res.append(queue.front())
        return res