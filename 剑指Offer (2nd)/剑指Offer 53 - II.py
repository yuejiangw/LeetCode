class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        right_nums = list(range(len(nums)+1))
        return sum(right_nums) - sum(nums)