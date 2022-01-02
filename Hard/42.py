from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        stack = []
        res = 0
        for i, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                curr_idx = stack.pop()
                while stack and height[stack[-1]] == height[curr_idx]:
                    stack.pop()
                if stack:
                    w = i - stack[-1] - 1
                    H = min(h, height[stack[-1]]) - height[curr_idx]
                    res += w * H
            stack.append(i)
        return res
