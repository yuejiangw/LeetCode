class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxNum = len(nums) * 0.5
        for i in set(nums):
            if nums.count(i) >= maxNum:
                return i
        return -1