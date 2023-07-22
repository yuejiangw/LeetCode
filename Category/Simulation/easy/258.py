class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)
        while len(num) != 1:
            summation = 0
            for c in num:
                summation += int(c)
            num = str(summation)
        return int(num)
