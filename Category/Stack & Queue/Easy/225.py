from collections import deque


class MyStack:
    """其实这道题一个队列就够了，在 pop 的时候把队列里的元素一个一个取出来再放回去就行了，需要借助 queue size 来实现。"""

    def __init__(self):
        self.queue_master = deque()
        self.queue_slave = deque()

    def push(self, x: int) -> None:
        self.queue_master.append(x)

    def pop(self) -> int:
        while len(self.queue_master) > 1:
            self.queue_slave.append(self.queue_master.popleft())
        res = self.queue_master.popleft()
        self.queue_master, self.queue_slave = self.queue_slave, self.queue_master
        return res

    def top(self) -> int:
        res = self.pop()
        self.queue_master.append(res)
        return res

    def empty(self) -> bool:
        return len(self.queue_master) == 0 and len(self.queue_slave) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
