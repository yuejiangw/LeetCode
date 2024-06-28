from typing import List

class Solution:
    # 最优算法，优化了单调栈所需的空间复杂度
    def findBuildings(self, heights: List[int]) -> List[int]:
        # T : O(N)
        # S: O(1)
        n = len(heights)
        res = [n - 1]
        max_height = heights[-1]
        for i in range(n - 2, -1, -1):
            if heights[i] > max_height:
                res.append(i)
                max_height = heights[i]
        res.reverse()
        return res

class Solution:
    # 常规单调栈
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        for i, height in enumerate(heights):
            while stack and stack[-1][1] <= height:
                stack.pop()
            stack.append((i, height))
        return [x[0] for x in stack]