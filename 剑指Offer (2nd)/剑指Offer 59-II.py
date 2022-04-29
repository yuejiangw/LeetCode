from collections import deque


class MaxQueue:
    # 单调队列，思路参考最小栈，用一个辅助的单调队列记录当前最大值
    # T: O(1)
    # S: O(N)
    def __init__(self):
        self.queue = deque()
        self.help = deque()
        self.size = 0

    def max_value(self) -> int:
        return -1 if self.size == 0 else self.help[0]

    def push_back(self, value: int) -> None:
        self.queue.append(value)
        while self.help and value > self.help[-1]:
            self.help.pop()
        self.help.append(value)
        self.size += 1

    def pop_front(self) -> int:
        if len(self.queue) == 0:
            return -1
        val = self.queue.popleft()
        if self.help and self.help[0] == val:
            self.help.popleft()
        self.size -= 1
        return val

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()