from collections import deque
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        op = ['+', '-', '*', '/']
        for char in tokens:
            if char not in op:
                stack.append(int(char))
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                if char == '+':
                    stack.append(n1 + n2)
                elif char == '-':
                    stack.append(n1 - n2)
                elif char == '*':
                    stack.append(n1 * n2)
                else:
                    stack.append(int(n1 / n2))
        return stack[0]
