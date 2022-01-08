class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        left_part = ['(', '{', '[']
        right_part = [')', '}', ']']
        stack = []
        for c in list(s):
            if c in left_part:
                stack.append(c)
            elif c in right_part:
                if stack == []:
                    stack.append(c)
                elif stack[-1] in left_part and \
                    right_part.index(c) == left_part.index(stack[-1]):
                    stack.pop(-1)
                else:
                    stack.append(c)
        return (stack == [])

from collections import deque
class Solution:
    """减小了解空间"""
    def isValid(self, s: str) -> bool:
        left = ['(', '[', '{']
        right = [')', ']', '}']
        stack = deque()
        for char in s:
            if char in left:
                stack.append(char)
            else:
                if len(stack) > 0 and stack[-1] in left and \
                right.index(char) == left.index(stack[-1]):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


class Solution:
    def isValid(self, s: str) -> bool:
        left_part = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if stack and stack[-1] == left_part[c]:
                    stack.pop()
                else:
                    stack.append(c)
        return stack == []
