class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                tmp = []
                # 处理栈顶元素直到遇到左括号
                while stack and stack[-1] != '(':
                    tmp.append(stack.pop())
                # 弹出左括号
                stack.pop()
                # 计算得分
                if len(tmp) == 0:
                    stack.append(1)
                else:
                    stack.append(sum(tmp) * 2)

        return sum(stack)
                