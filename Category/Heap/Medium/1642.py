from typing import List
from heapq import heappush, heappop

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # T: O(nlogn)
        # S: O(n)
        height_diff_heap = []
        for i in range(len(heights) - 1):
            curr, next = heights[i], heights[i + 1]
            diff = next - curr

            # 当前楼的高度大于等于下一栋楼的高度，直接跳过
            if diff <= 0:
                continue
            
            # 有梯子优先使用梯子，梯子用完了之后先判断能否使用砖头，如果不能的话尝试匀一个梯子出来
            heappush(height_diff_heap, diff)
            if len(height_diff_heap) > ladders:
                bricks -= heappop(height_diff_heap)
                if bricks < 0:
                    return i
        return len(heights) - 1