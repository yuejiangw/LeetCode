class Solution:
    def minInsertions(self, s: str) -> int:
        left_need = 0   # 左括号需求
        right_need = 0  # 右括号需求
        for c in s:
            if c == '(':
                # 一个左括号需要两个右括号来匹配
                right_need += 2
                # 因为是 minimum insertion，所以尽可能把 right_need 转化为 left_need
                if right_need % 2 == 1:
                    left_need += 1
                    right_need -= 1
            else:
                right_need -= 1
                # 多出来一个右括号
                if right_need == -1:
                    right_need = 1
                    left_need += 1
        return left_need + right_need