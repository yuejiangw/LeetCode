class Solution:
    op_priority = {'+': 0, '-': 0, '*': 1, '/': 1, '%': 1, '^': 2}

    def calc(self, num_stack: list, op_stack: list) -> None:
        if not op_stack or len(num_stack) < 2:
            return
        op, y, x = op_stack.pop(), num_stack.pop(), num_stack.pop()
        ans = 0
        if op == '+':
            ans = x + y
        elif op == '-':
            ans = x - y
        elif op == '*':
            ans = x * y
        elif op == '/':
            ans = x / y
        elif op == '%':
            ans = x % y
        elif op == '^':
            ans = pow(x, y)
        num_stack.append(int(ans))

    def calculate(self, s: str) -> int:
        s = "(" + s.replace(" ", "").replace("(-", "(0-") + ")"
        n = len(s)
        # operators & numbers
        op_stack, num_stack = [], []

        i = 0
        while i < n:
            c = s[i]
            i += 1

            if c.isdigit():  # a number
                num = int(c)
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                num_stack.append(num)
            elif c == '(':  # (
                op_stack.append(c)
            elif c == ')':  # calculate until see '('
                while op_stack and op_stack[-1] != '(':
                    self.calc(num_stack, op_stack)
                op_stack.pop()
            else:
                while op_stack and op_stack[-1] != '(':
                    prev_op = op_stack[-1]
                    if self.op_priority[prev_op] < self.op_priority[c]:
                        break
                    self.calc(num_stack, op_stack)
                op_stack.append(c)

        return num_stack[0]
