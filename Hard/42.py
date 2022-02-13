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


class Solution:
    """ 
    单调栈思路:
    栈内存放的是各个雨水的下标, 
    """
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        stack = []
        res = 0
        for i, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                curr_width = i - left - 1
                curr_height = min(height[left], h) - height[top]
                res += curr_height * curr_width
            stack.append(i)
        return res
