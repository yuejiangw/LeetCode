class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        right = set()
        left = []
        for i, c in enumerate(s):
            if c == '(':
                left.append(i)
            elif c == ')':
                if left:
                    left.pop()
                else:
                    right.add(i)
        need_remove = set(left) | set(right)
        return ''.join([c for i, c in enumerate(s) if i not in need_remove])
