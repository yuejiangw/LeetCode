class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        res = 0
        pre_bracket = 0
        i = 0
        while i < len(brackets):
            bracket, percent = brackets[i]
            if income <= bracket:
                res += (income - pre_bracket) * percent
                break
            else:
                res += (bracket - pre_bracket) * percent
                pre_bracket = bracket
                i += 1
        # 把浮点运算放在最后
        return res / 100
        