class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        visited = set()
        for i, c in enumerate(s):
            if c in visited:
                continue
            while stack and stack[-1] > c and (stack[-1] in s[i+1:]):
                visited.remove(stack.pop())
            stack.append(c)
            visited.add(c)
        return ''.join(stack)
