from collections import deque
from typing import List


class MonotonicQueue:
    def __init__(self):
        self.queue = deque()

    def push(self, num):
        while self.queue and num > self.queue[-1]:
            self.queue.pop()
        self.queue.append(num)

    def max(self):
        return self.queue[0]

    def pop(self, num):
        if num == self.queue[0]:
            self.queue.popleft()


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = MonotonicQueue()
        res = []
        for i, num in enumerate(nums):
            if i < k - 1:
                queue.push(num)
            else:
                queue.push(num)
                res.append(queue.max())
                queue.pop(nums[i - k + 1])
        return res
