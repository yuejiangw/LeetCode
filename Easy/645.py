class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # n1为重复的值
        n1 = sum(nums) - sum(set(nums))
        # n2为正确的值
        n2 = sum(range(len(nums)+1)) - sum(set(nums))
        return [n1, n2]