class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0     # 记录对左括号的需求数
        need = 0    # 记录对右括号的需求数，根据 need 来判断是否需要插入
        for c in s:
            if c == '(':
                # 一个左括号需要匹配两个右括号
                need += 2
                if need % 2 == 1:
                    # 如果右括号的数量变成了奇数则需要插入一个右括号
                    res += 1
                    need -= 1
            elif c == ')':
                need -= 1
                if need == -1:
                    # 多出来一个右括号，需要插入一个左括号和一个右括号来匹配
                    res += 1
                    need = 1
        return res + need