from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        # 每个元素辐射的左右边界
        left, right = [0] * n, [0] * n
        
        # 找左边界
        stack = []
        for i in range(n):
            # 向左找第一个小于等于 arr[i] 的元素
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            left[i] = -1 if not stack else stack[-1]
            stack.append(i)
        
        # 找右边界
        stack = []
        for i in range(n - 1, -1, -1):
            # 向右找第一个小于 arr[i] 的元素
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            right[i] = n if not stack else stack[-1]
            stack.append(i)
        
        res = 0
        for i in range(n):
            res += (i - left[i]) * (right[i] - i) * arr[i]
        return res % (10**9 + 7)