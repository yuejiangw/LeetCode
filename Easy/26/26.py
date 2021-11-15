# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         nums2 = nums.copy()
#         for i in nums2:
#             if (nums.count(i) == 1):
#                 continue
#             else:
#                 nums.remove(i)
#         return len(nums)


# 其实就是双指针的思想，用 j 去找有没有和 i 相同的元素；
# 如果有的话，那么需要将 j 右移；
# 如果没有的话，那么需要将 j 所指元素赋值给 i + 1 所指元素；
# 只有这样才能将之前重复的元素给覆盖；
# 最后返回 i + 1 即可，其表示非重复元素的个数。
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1
        while j < len(nums):
            if nums[j] == nums[i]:
                j += 1
            else:
                nums[i + 1] = nums[j]
                i += 1
                j += 1
        return i + 1

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i, j = 1, 1
        while j < len(nums):
            if nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i