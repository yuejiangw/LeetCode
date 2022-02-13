import heapq
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """ 小顶堆 """
        heap = []
        for num in arr:
            # heappush 接受两个参数，第一个是 heap，第二个是 element
            # 当 element 为元组时，会以 element[0] 作为 key 进行排序
            # 由题意得，key 应该为 (abs(num - x), num)，代表默认情况
            # 下以绝对值之差作为比较器，有冲突时按照 num 的大小进行排序
            heapq.heappush(heap, ((abs(num - x), num), num))
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return sorted(res)

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """ 排序 """
        arr = sorted(arr, key=lambda n: (abs(n - x), n))
        return sorted(arr[:k])
