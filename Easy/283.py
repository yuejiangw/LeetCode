class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_num = nums.count(0)
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                del nums[i]
            else:
                i += 1
        nums += [0 for i in range(zero_num)]