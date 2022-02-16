from typing import List
from collections import deque


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        total_sum = sum(changed)
        length = len(changed)
        if total_sum % 3 != 0 or length % 2 == 1:
            return []
        
        changed.sort()
        # 排序后按顺序遍历，原值 x 与双倍值 y 一定按顺序排列在一起
        # 且 x 一定都在 y 的前面
        res = []
        queue = deque()
        for num in changed:
            if queue and num == 2 * queue[0]:
                res.append(queue.popleft())
            else:
                queue.append(num)
        return [] if queue else res