from collections import deque

class HitCounter:

    def __init__(self):
        self.queue = deque()

    def hit(self, timestamp: int) -> None:
        while self.queue and self.queue[0] + 300 <= timestamp:
            self.queue.popleft()
        self.queue.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.queue and self.queue[0] + 300 <= timestamp:
            self.queue.popleft()
        return len(self.queue)

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)