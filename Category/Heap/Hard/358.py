from collections import deque, Counter
from heapq import *


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        # Greedy 
        # 优先填入出现次数多的字符，这样可以使其可选择下标的范围增大
        # 为了得到出现次数多的字符可以使用大顶堆，堆的顶部为出现次数最多且字典序最小的元素
        if k < 2:
            return s
        cnt = Counter(s)
        heap = []
        for c, count in cnt.items():
            heappush(heap, [-count, c])
        queue = deque([])

        res = ''
        # 这里需要注意的是，在不断插入字符的过程中，由于 count 变小，那么当前字符的优先级可能会改变，因此要根据 count 动态调整堆顶元素
        while heap:
            count, c = heappop(heap)
            count = -count

            res += c
            queue.append((count -1, c))

            # 距离上一个相同字符已经过去 k 步了，则后移窗口重新组织堆
            if len(queue) == k:
                count, c = queue.popleft()
                if count > 0:
                    heappush(heap, [-count, c])

        return res if len(res) == len(s) else ''