class Solution:
    def getDigits(self, n: int) -> List[int]:
        result = []
        tmp = str(n)
        for s in tmp:
            result.append(int(s))
        return result

    def subtractProductAndSum(self, n: int) -> int:
        digits = self.getDigits(n)
        result1 = 1
        for digit in digits:
            result1 *= digit
        result2 = sum(digits)
        return result1 - result2