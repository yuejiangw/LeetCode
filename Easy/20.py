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