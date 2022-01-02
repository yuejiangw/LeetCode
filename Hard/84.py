from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        stack = []
        # 为了便于处理边界，在 heights 的左右两端分别插入一个0
        heights.insert(0, 0)
        heights.append(0)
        res = 0
        for i, height in enumerate(heights):
            # 单调递增栈，如果当前元素比栈顶元素小，则出栈
            w = 0
            h = float('inf')
            while stack and height < heights[stack[-1]]:
                curr_idx = stack.pop()
                curr_height = heights[curr_idx]
                res = max(res, (i - stack[-1] - 1) * curr_height)
            stack.append(i)

        return res
