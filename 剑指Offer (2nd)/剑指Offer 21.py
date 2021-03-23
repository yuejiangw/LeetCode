class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        result = []
        i = 0
        while i < len(nums):
            if nums[i] % 2 == 1:
                result.append(nums[i])
                del nums[i]
            else:
                i += 1
        result += nums
        return result