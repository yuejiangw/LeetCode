class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        num = 0
        digits.reverse()
        for i in range(len(digits)):
            num += digits[i] * pow(10, i)
        num += 1
        result = []
        while num != 0:
            result.insert(0, num % 10)
            num = num // 10
        return result