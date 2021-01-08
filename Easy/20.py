class Solution:
    def isValid(self, s: str) -> bool: 
        if not s:
            return False
        leftPart = ['(', '[', '{']
        rightPart = [')', ']', '}']
        stack = []
        for char in s:
            if char in leftPart:
                stack.append(char)
            if char in rightPart:
                if stack == []:
                    stack.append(char)
                elif stack[-1] in leftPart and \
                    rightPart.index(char) == leftPart.index(stack[-1]):
                    stack.pop()
                else:
                    stack.append(char)
        return stack == []
