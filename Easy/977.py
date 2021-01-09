class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        newNums = [abs(num) for num in nums]
        newNums.sort()
        return [n ** 2 for n in newNums]