from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        # 用队列模拟窗口
        # 时间复杂度 O(1) 空间复杂度 O(size)
        self.queue = deque()
        self.size = size
        self.total = 0
        self.length = 0

    def next(self, val: int) -> float:
        self.total += val
        self.queue.append(val)
        self.length += 1
        if self.length > self.size:
            self.total -= self.queue.popleft()
            self.length -= 1
        return self.total / self.length


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)