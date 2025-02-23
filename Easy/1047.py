class Solution:
    def removeDuplicates(self, s: str) -> str:
        # T: O(n), S: O(n)
        stack = []
        for c in s:
            if not stack or stack[-1] != c:
                stack.append(c)
            else:
                while stack and stack[-1] == c:
                    stack.pop()
        return ''.join(stack)