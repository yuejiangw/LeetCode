from collections import deque
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = deque()
        for char in s:
            if len(stack) == 0:
                stack.append(char)
            else:
                if stack[-1] != char:
                    stack.append(char)
                else:
                    stack.pop()
        return ''.join(stack)
