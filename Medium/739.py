class Solution:
    def dailyTemperatures(self, T):
        '''单调栈'''
        stack = []
        result = [0] * len(T)
        for index, tmp in enumerate(T):
            if stack == []:
                stack.append((index, tmp))
            else:
                # 如果当前元素大于栈顶元素，则栈顶元素出栈，同时将、
                # result中的index位置更新为两个index之差，之后当前元素入栈
                while len(stack) > 0 and tmp > stack[-1][1]:
                    stack_head = stack.pop(-1)
                    result[stack_head[0]] = index - stack_head[0]
                stack.append((index, tmp))   
        # 如果最后栈非空，则栈内元素都对应0
        while stack:
            curr = stack.pop(-1)
            result[curr[0]] = 0
        return result