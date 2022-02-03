class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # Use a stack to store the characters and their related counts.
        # When there are k same characters, delete them.
        stack = []
        for char in s:
            if not stack or (stack is not None and stack[-1][0] != char):
                stack.append([char, 1])
            elif stack[-1][0] == char:
                stack[-1][1] += 1

            if stack[-1][1] == k:
                stack.pop()
        return ''.join([x[0] * x[1] for x in stack])
