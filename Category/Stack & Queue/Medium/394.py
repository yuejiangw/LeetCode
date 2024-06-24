from collections import deque
class Solution:
    def decodeString(self, s: str) -> str:
        def isDigit(c):
            return c >= '0' and c <= '9'
        
        def isChar(c):
            return (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z')

        deq = deque()
        i = 0
        while i < len(s):
            # 当前字符是字母或'['，则正常入栈
            if isChar(s[i]) or s[i] == '[':
                deq.append(s[i])
                i += 1
            # 当前字符是数字，则向后解析相连的全部数字，并入栈
            elif isDigit(s[i]):
                num = ''
                while isDigit(s[i]):
                    num += s[i]
                    i += 1
                num = int(num)
                deq.append(num)
            # 当前字符是']'，则出栈直到最近的'['也出栈，之后与前一个数字拼接
            elif s[i] == ']':
                # 出栈
                tmp_str = ''
                while deq[-1] != '[':
                    tmp_str = deq.pop() + tmp_str
                deq.pop()
                deq.append(deq.pop() * tmp_str)
                i += 1
        result = ''
        while deq:
            result += deq.popleft()
        return result


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            # If current char is '[' or a normal English letter,
            # then push it into stack directly.
            if s[i] == '[' or 'a' <= s[i] <= 'z':
                stack.append(s[i])
                i += 1
            # If current char is a number, then parse the following
            # characters until we reach a non-number character.
            elif s[i].isdigit():
                start = i
                while s[i].isdigit():
                    i += 1
                stack.append(int(s[start: i]))
            # If current char is ']', then pop from the stack until we meet a '['
            elif s[i] == ']':
                tmp = ''
                while stack[-1] != '[':
                    tmp = stack.pop() + tmp
                stack.pop()
                stack.append(stack.pop() * tmp)
                i += 1
        return ''.join(stack)
