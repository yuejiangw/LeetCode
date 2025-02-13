class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # 最优解，时间复杂度 O(n)，空间复杂度 O(1)
        left = 0
        right_need = 0
        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                if left > 0:
                    left -= 1
                else:
                    right_need += 1
        return left + right_need


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(c)
        return len(stack)
