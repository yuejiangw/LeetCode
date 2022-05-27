class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # T: O(n)
        # S: O(1)
        l = 0
        res = ''
        for char in s:
            if char == '(':
                l += 1
                if l > 1:
                    res += char
            else:
                if l > 1:
                    res += char
                l -= 1
        return res
