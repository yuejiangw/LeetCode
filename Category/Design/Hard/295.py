from heapq import *


class MedianFinder:

    def __init__(self):
        self.max_h = []  # 大顶堆，储存较小一半元素
        self.min_h = []  # 小顶堆，储存较大一半元素
        heapify(self.max_h)
        heapify(self.min_h)

    def addNum(self, num: int) -> None:
        """
        每次插入到小顶堆，然后将最小堆中的栈顶元素取出来放到大顶堆，
        这样可以保证小顶堆中的全部元素都要大于大顶堆中的全部元素.
        对于 heapq 实现大顶堆，可以插入num的相反数，取出来的时候也
        取相反数即可
        """
        heappush(self.min_h, num)
        heappush(self.max_h, -heappop(self.min_h))
        if len(self.min_h) < len(self.max_h):
            heappush(self.min_h, -heappop(self.max_h))

    def findMedian(self) -> float:
        length = len(self.max_h) + len(self.min_h)
        return self.min_h[0] if length % 2 == 1 else (
            self.min_h[0] + -self.max_h[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
