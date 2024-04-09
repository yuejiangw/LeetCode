from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = i + (j - i) // 2
            if nums[mid] == target:
                return mid
            # 中间的数小于右端点的数，说明 mid 右半部分是有序的
            elif nums[mid] < nums[j]:
                if nums[mid] < target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1
            # 中间的数大于右端点的数，说明 mid 左半部分是有序的
            else:
                if nums[i] <= target < nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1 
        return -1