class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        for i in range(n):
            nums.append(start + 2 * i)
        result = nums[0]
        for j in range(1, n):
            result = result ^ nums[j]
        return result