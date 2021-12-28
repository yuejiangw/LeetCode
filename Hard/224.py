class Solution:
    def compute(self, num_stack, op_stack):
        if len(num_stack) < 2 or not op_stack:
            return
        y, x = num_stack.pop(), num_stack.pop()
        op = op_stack.pop()
        res = 0
        if op == '+':
            res = x + y
        elif op == '-':
            res = x - y
        num_stack.append(res)

    def calculate(self, s: str) -> int:
        op_prio = {'+': 1, '-': 1}
        s = '(' + s.replace(' ', '') + ')'
        s = s.replace("(-", "(0-")
        num_stack, op_stack = [], []
        n = len(s)
        i = 0
        while i < n:
            c = s[i]
            i += 1

            if c.isdigit():
                num = int(c)
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                num_stack.append(num)

            elif c == '(':
                op_stack.append(c)

            elif c == ')':
                while op_stack and op_stack[-1] != '(':
                    self.compute(num_stack, op_stack)
                op_stack.pop()

            else:
                while op_stack and op_stack[-1] != '(':
                    pre_op = op_stack[-1]
                    if op_prio[pre_op] < op_prio[c]:
                        break
                    self.compute(num_stack, op_stack)
                op_stack.append(c)
        return num_stack[0]
