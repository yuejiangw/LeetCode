class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        visited = set()

        for i, c in enumerate(s):
            if c in visited:
                continue
            # 如果栈顶元素比当前访问的字符要大，并且在当前字符后面还有栈顶元素，则出栈
            while stack and stack[-1] > c and (stack[-1] in s[i+1:]):
                visited.remove(stack.pop())

            stack.append(c)
            visited.add(c)
        return ''.join(stack)
