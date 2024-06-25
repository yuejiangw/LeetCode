from typing import List
import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """ 思路: 找第 k 小, 借助小顶堆 """
        n = len(matrix)
        nums = [(matrix[i][0], i, 0) for i in range(n)]  # 取出第一列元素
        # 其中 matrix[i][0] 是元素, 后面的 (i, 0) 是坐标
        heapq.heapify(nums)

        for _ in range(k - 1):
            num, x, y = heapq.heappop(nums)
            if y != n - 1:
                heapq.heappush(nums, (matrix[x][y + 1], x, y + 1))
        return nums[0][0]
