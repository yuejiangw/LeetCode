from collections import deque;

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def stack_help(s):
            stack = deque()
            for i in range(len(s)):
                if s[i] != '#':
                    stack.append(s[i])
                else:
                    if len(stack) != 0:
                        stack.pop()
            return ''.join(stack)
        return stack_help(s) == stack_help(t)
