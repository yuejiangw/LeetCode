class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        res = 0
        stack = []
        for char in s:
            if char == '(':
                max_depth += 1
            elif char == ')':
                max_depth -= 1
            res = max(res, max_depth)
        return res
