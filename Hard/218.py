from sortedcontainers import SortedList
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # T: O(nlogn)
        # S: O(n)
        ans = []

        # 预处理所有的点，为了方便排序，对于左端点，令高度为负；对于右端点令高度为正
        ps = []
        for l, r, h in buildings:
            ps.append((l, - h))
            ps.append((r, h))
        # 先按照横坐标进行排序
        # 如果横坐标相同，则按照左端点排序
        # 如果相同的左/右端点，则按照高度进行排序
        ps.sort()

        prev = 0
        # 有序列表充当大根堆
        q = SortedList([prev])

        for point, height in ps:
            if height < 0:
                # 如果是左端点，说明存在一条往右延伸的可记录的边，将高度存入优先队列
                q.add(-height)
            else:
                # 如果是右端点，说明这条边结束了，将当前高度从队列中移除
                q.remove(height)
            
            # 取出最高高度，如果当前不与前一矩形“上边”延展而来的那些边重合，则可以被记录
            cur = q[-1]
            if cur != prev:
                ans.append([point, cur])
                prev = cur

        return ans